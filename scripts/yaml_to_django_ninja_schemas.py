# scripts/yaml_to_django_ninja_schemas.py

import os
import yaml
import keyword
import textwrap
from collections import defaultdict

# --- Configuration ---
YAML_SCHEMA_DIR = os.path.join(os.path.dirname(__file__), '..', 'schema')
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'conversions', 'django_ninja_schemas')
BASE_PROPERTIES_FILE = 'base_properties.yaml'
BASE_SCHEMAS_FILENAME = 'base_schemas.py'

# --- Helper Functions ---

def safe_load_yaml(filepath):
    """Loads a YAML file safely."""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        print(f"Error: YAML file not found at {filepath}")
        return None
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file {filepath}: {e}")
        return None

def get_python_type_hint(yaml_type_details, context="base", is_required=False):
    """Maps YAML type details to Python type hints for Ninja schemas.
       Uses `| None` instead of `Optional` unless `is_required` is True for base context.
    """
    yaml_type = yaml_type_details.get('type') if isinstance(yaml_type_details, dict) else yaml_type_details

    if not yaml_type:
        return "Any" if is_required and context == "base" else "Any | None"

    optional_suffix = "" if is_required and context == "base" else " | None"

    # Types for Base/In/Update Schemas (influenced by is_required)
    if context == "base":
        if yaml_type == 'string':
            return f"str{optional_suffix}"
        elif yaml_type == 'integer':
            return f"int{optional_suffix}"
        elif yaml_type == 'boolean':
            return f"bool{optional_suffix}"
        elif yaml_type == 'number':
            return f"float{optional_suffix}"
        elif yaml_type == 'single-link':
             # UUID itself is not optional, the field is.
            return f"uuid.UUID{optional_suffix}"
        elif yaml_type == 'multi-link':
             # List structure itself isn't optional, but the field can be None
            return f"list[uuid.UUID]{optional_suffix}"
        elif yaml_type == 'array':
             # Get the base type hint for the item, assuming items themselves aren't required *within* the list
            item_type_hint = get_python_type_hint(yaml_type_details.get('items', {'type': 'string'}), context, is_required=False)
            item_type_base = item_type_hint.replace(" | None", "") # Item type within list shouldn't be optional unless specified
            return f"list[{item_type_base}]{optional_suffix}"

    # Types for Out Schemas (generally keep optional unless it's a list)
    elif context == "out":
         if yaml_type == 'string': return "str | None"
         if yaml_type == 'integer': return "int | None"
         if yaml_type == 'boolean': return "bool | None"
         if yaml_type == 'number': return "float | None"
         # Links handled elsewhere for Out schema (become nested)
         # Non-link types fall through to base logic but without required affecting them
         return get_python_type_hint(yaml_type_details, context="base", is_required=False)

    # Fallback for simple types defined directly (like in base_properties)
    if isinstance(yaml_type, str):
        if yaml_type.lower() == 'string': return f"str{optional_suffix}"
        if yaml_type.lower() == 'integer': return f"int{optional_suffix}"
        if yaml_type.lower() == 'url': return f"str{optional_suffix}"
        if yaml_type.lower() == 'uuid': return "uuid.UUID" # UUID primary key is never optional

    # Default fallback
    return "Any" if is_required and context == "base" else "Any | None"

def generate_field_definition(field_name, yaml_details, imports_tracker, context="base", alias=None, is_required=False):
    """Generates a Ninja schema field definition string."""
    # Pass is_required to get the correct type hint
    py_type_hint = get_python_type_hint(yaml_details, context=context, is_required=is_required)
    py_field_name = field_name # Use the name passed in

    field_args = []
    field_args_str = ""
    default_assignment = "" # Will be empty for required fields

    # Determine default assignment string based on type hint and context
    if not is_required or context != "base": # Only add default if not required in base context
        if context == 'out' and py_type_hint.startswith('list['):
            default_value = "[]"
            default_assignment = f" = {default_value}"
        elif " | None" in py_type_hint: # Check if the final type hint allows None
             default_value = "None"
             default_assignment = f" = {default_value}"
        # If required, default_assignment remains ""

    # Handle explicit alias (usually for base properties like Image_URL)
    if alias:
        field_args.append(f"alias='{alias}'")
        imports_tracker['Field'] = "from ninja import Field"

    # Handle constraints (only 'maximum' for 'le' currently)
    maximum = yaml_details.get('maximum') if isinstance(yaml_details, dict) else None
    if maximum is not None and isinstance(maximum, (int, float)) and maximum > 0:
        constraint_args = [f"le={maximum}"]
        # If we already have an alias, append constraint
        if field_args:
             field_args.extend(constraint_args)
        # If no alias, but the field is optional, add None first
        elif not is_required and (" | None" in py_type_hint or default_assignment == " = None"):
            field_args = ["None"] + constraint_args
        # Otherwise (required or non-optional type with constraint), just add constraint
        else:
             field_args = constraint_args
        imports_tracker['Field'] = "from ninja import Field"

    # Build Field string if needed
    if field_args:
        # Check if default 'None' should be the first arg if field is optional and not already added
        if not is_required and (" | None" in py_type_hint or default_assignment == " = None") and (not field_args or "None" not in field_args[0]):
             # Ensure "None" is the first argument for optional fields when using Field(...)
             if "None" not in field_args: # Avoid duplicates if added by constraint logic
                 field_args.insert(0, "None")

        field_args_str = ", ".join(field_args)
        return f"{py_field_name}: {py_type_hint} = Field({field_args_str})"
    else:
        # Simple assignment with conditional default
        return f"{py_field_name}: {py_type_hint}{default_assignment}"


def get_nested_out_field_name(yaml_field_name, yaml_link_type):
    """Determines the field name for nested objects in OutSchema."""
    # Use the raw field name from YAML directly for nested output
    return yaml_field_name


# --- Schema Generation Logic ---

def generate_base_schemas(base_yaml_path, output_file):
    """Generates the base_schemas.py file."""
    base_yaml = safe_load_yaml(base_yaml_path)
    if not base_yaml or 'properties' not in base_yaml:
        print("Error: Could not load or parse base properties YAML.")
        return

    # Match target import style
    imports_content = textwrap.dedent("""\
        from ninja import Field, Schema, FilterSchema # type: ignore
        from typing import List # Only List needed now
        import uuid
    """)

    base_fields = []
    nested_out_fields = []
    base_properties = base_yaml.get('properties', {})
    required_base_fields = base_yaml.get('required', []) # Read required fields
    imports_tracker = defaultdict(str) # Track needed imports like Field

    # Generate AbstractElementBaseSchema
    for field, details in base_properties.items():
        py_field_name = field.lower()
        is_required = field in required_base_fields # Check if field is required

        # --- Generate field definition for Base Schema ---
        field_def = ""
        py_explicit_alias = None
        if field != py_field_name: # Original name differs (e.g., Image_URL)
            py_explicit_alias = field

        # Special handling for id, name, world which have specific requirements
        if py_field_name == 'id':
            field_def = f"id: uuid.UUID" # Always required
        elif py_field_name == 'name':
             field_def = f"name: str" # Always required
        elif py_field_name == 'world':
             # World is conceptually required for an element, but represented by UUID
             # Keep it optional in base schema for flexibility? Let's make it required.
             field_def = f"world: uuid.UUID" # Changed to required
        else:
            # Use generate_field_definition for other fields
            field_def = generate_field_definition(
                py_field_name,
                details,
                imports_tracker,
                context="base",
                alias=py_explicit_alias,
                is_required=is_required
            )

        base_fields.append(field_def)

        # --- Define fields for NestedOutSchema (remains mostly the same) ---
        if py_field_name in ['id', 'name', 'supertype', 'subtype', 'image_url']:
             if py_field_name == 'id':
                 nested_out_fields.append(f"id: uuid.UUID")
             elif py_field_name == 'name':
                 nested_out_fields.append(f"name: str")
             elif py_field_name == 'image_url' and field != py_field_name:
                 nested_out_fields.append(f"{py_field_name}: str | None = Field(None, alias='{field}')")
                 # Ensure Field is tracked if used here, though likely caught by base schema generation
                 if 'Field' not in imports_tracker: imports_tracker['Field'] = "from ninja import Field"
             else:
                 nested_out_fields.append(f"{py_field_name}: str | None = None")


    # Ensure Field import is added if used
    if imports_tracker['Field'] and 'Field' not in imports_content:
         # This logic might need refinement based on final import structure
         imports_content += "\n" + imports_tracker['Field'] # Basic append for now

    content = ""
    content += imports_content + "\n\n" # Use the defined import block

    content += "class AbstractElementBaseSchema(Schema):\n"
    # content += '    """Base schema reflecting fields from common.AbstractElementModel."""\n' # Remove docstring
    content += textwrap.indent("\n".join(base_fields), "    ") + "\n\n\n"

    content += "class ElementNestedOutSchema(Schema):\n"
    # content += '    """Minimal schema for representing elements nested within other responses."""\n' # Remove docstring
    content += textwrap.indent("\n".join(nested_out_fields), "    ") + "\n\n\n"

    # Add BaseFilterSchema
    content += "class BaseFilterSchema(FilterSchema):\n"
    content += '    """Base filter schema including common element fields."""\n'
    content += "    name__icontains: str | None = Field(None, q='name__icontains')\n" # Changed to | None
    content += "    supertype: str | None = Field(None, q='supertype')\n" # Changed to | None
    content += "    subtype: str | None = Field(None, q='subtype')\n" # Changed to | None

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Generated {output_file}")


def generate_category_schema(category_name, category_yaml_path, output_file):
    """Generates a specific category's schema file (e.g., character_schemas.py)."""
    category_yaml = safe_load_yaml(category_yaml_path)
    if not category_yaml or 'properties' not in category_yaml:
        print(f"Warning: Skipping {category_name}. Could not load or parse YAML.")
        return

    class_name_base = category_name.capitalize()

    # Define needed imports based on target file structure
    imports_needed = {
        'base': f"from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema",
        'ninja': "from ninja import Field, FilterSchema  # type: ignore", # Assuming Field/Filter always needed
        'typing_List': "from typing import List",
        'uuid': "import uuid"
    }
    # Track which specific imports are actually used by the fields generated
    imports_tracker = defaultdict(bool)
    imports_tracker['base'] = True # Always needed
    imports_tracker['ninja'] = True # Assume always needed
    imports_tracker['uuid'] = True # Assume always needed

    base_schema_fields_dict = defaultdict(list)
    out_schema_fields_dict = defaultdict(list)
    filter_schema_fields = []

    # Process fields and group by section
    for section, section_data in category_yaml.get('properties', {}).items():
        if isinstance(section_data, dict) and 'properties' in section_data:
            nested_properties = section_data['properties'] # Get nested props
            nested_required = section_data.get('required', []) # Get required list for this section

            for field, details in nested_properties.items(): # Use nested_properties here
                yaml_link_type = details.get('type') if isinstance(details, dict) else None
                original_field_name = field
                is_field_required = original_field_name in nested_required # Check requirement

                # Determine the python field name for use in the schema definition
                # And the alias if the python name differs from the original yaml key
                py_schema_name = original_field_name
                py_explicit_alias_for_base = None # Alias ONLY needed if name changes (e.g. Image_URL)
                # py_alias_name_for_out = None # We won't use aliases for keywords/links in OutSchema

                if keyword.iskeyword(original_field_name):
                    # Rename consistently by prepending category name (lowercase)
                    py_schema_name = f"{category_name.lower()}_{original_field_name}";
                    # No alias needed as the name is changed everywhere
                    # py_alias_name_for_base = original_field_name # Removed
                    # py_alias_name_for_out = original_field_name # Removed

                # Determine names specific to links, overriding py_schema_name for *Base* schema
                py_schema_name_for_base_link = py_schema_name # Start with potentially keyword-modified name
                if yaml_link_type == 'single-link':
                    py_link_name = f"{py_schema_name}_id" # Use the potentially modified name + _id
                    # Example: if original was 'class', py_schema_name is 'character_class', py_link_name is 'character_class_id'
                    py_schema_name_for_base_link = py_link_name # Use the link name (_id) for BaseSchema
                    # Alias is *only* needed for OutSchema to map back, unless already set for keyword
                    # if not py_alias_name_for_out:
                    #      py_alias_name_for_out = original_field_name # Removed logic
                elif yaml_link_type == 'multi-link':
                    py_link_name = f"{py_schema_name}_ids" # Use the potentially modified name + _ids
                    # Example: if original was 'items', py_schema_name is 'category_items', py_link_name is 'category_items_ids'
                    py_schema_name_for_base_link = py_link_name # Use the link name (_ids) for BaseSchema
                    # Alias is *only* needed for OutSchema to map back, unless already set for keyword
                    # if not py_alias_name_for_out:
                    #      py_alias_name_for_out = original_field_name # Removed logic

                # Use the potentially link-modified name for the final Base schema name
                py_final_schema_name_for_base = py_schema_name_for_base_link
                # Use the non-link name (but potentially keyword-modified) for the Out schema name
                py_final_schema_name_for_out = py_schema_name


                # --- Field for Base Schema --- (Pass is_required)
                field_def_base = generate_field_definition(
                    py_final_schema_name_for_base, details, imports_tracker, context="base", alias=py_explicit_alias_for_base,
                    is_required=is_field_required # Pass the flag here
                )
                base_schema_fields_dict[section].append(field_def_base)
                if 'list[' in field_def_base: imports_tracker['typing_list_primitive'] = True
                if 'uuid.UUID' in field_def_base: imports_tracker['uuid'] = True

                # --- Field for Out Schema ---

                if yaml_link_type == 'single-link':
                    # Use py_final_schema_name_for_out (original name or keyword_)
                    # No alias needed. Default is None.
                    out_schema_fields_dict[section].append(f"{py_final_schema_name_for_out}: ElementNestedOutSchema | None = None")
                    # imports_tracker['typing_Optional'] = True # No longer needed
                    # Filter field uses the base schema name (_id) for the schema field definition
                    # and the same base schema name (_id) for q lookup
                    filter_schema_fields.append(f"{py_schema_name_for_base_link}: uuid.UUID | None = Field(None, q='{py_schema_name_for_base_link}')") # Use base name for field and q
                elif yaml_link_type == 'multi-link':
                    # Use py_final_schema_name_for_out (original name or keyword_)
                    # No alias needed. Default is [].
                    out_schema_fields_dict[section].append(f"{py_final_schema_name_for_out}: List[ElementNestedOutSchema] = []")
                    imports_tracker['typing_List'] = True
                    # Filter field uses the base schema name (_ids) for the schema field definition
                    # but uses original field name + __id for q lookup on the M2M field
                    filter_schema_fields.append(f"{py_schema_name_for_base_link}: uuid.UUID | None = Field(None, q='{original_field_name}__id')") # Use base name for field, original_name__id for q
                else:
                    # Regular field - generate using py_final_schema_name_for_out
                    # Pass alias ONLY if explicitly needed (e.g. Image_URL, not for keywords)
                    field_def_out = generate_field_definition(
                         py_final_schema_name_for_out, details, imports_tracker, context="out", alias=py_explicit_alias_for_base # Use base alias here if it was explicit (e.g. Image_URL)
                    )
                    out_schema_fields_dict[section].append(field_def_out)

    # Build import string based on tracked usage
    final_import_lines = [imports_needed['base']]
    if imports_tracker['ninja']: final_import_lines.append(imports_needed['ninja'])
    # Combine List/Optional imports if both needed
    typing_imports = []
    if imports_tracker['typing_List'] or imports_tracker['typing_list_primitive']:
         typing_imports.append("List")
    # Optional removed

    if typing_imports:
        final_import_lines.append(f"from typing import {', '.join(typing_imports)}")

    if imports_tracker['uuid']: final_import_lines.append(imports_needed['uuid'])
    # Sort or order imports as per target file? Example seems semi-ordered.
    # final_import_lines.sort() # Optional: sort imports alphabetically

    content = ""
    # Adjusting order slightly based on target example
    ordered_imports = [imports_needed['base'], imports_needed['ninja']]
    if typing_imports: ordered_imports.append(f"from typing import {', '.join(typing_imports)}")
    ordered_imports.append(imports_needed['uuid'])
    content += "\n".join(ordered_imports) + "\n\n\n"


    # --- <Category>BaseSchema ---
    content += f"class {class_name_base}BaseSchema(AbstractElementBaseSchema):\n"
    for section, fields in base_schema_fields_dict.items():
         content += f"\n    # {section.capitalize()}\n" # Indented section comment
         content += textwrap.indent("\n".join(fields), "    ") + "\n"
    content += "\n\n" # Extra newline after class

    # --- <Category>CreateInSchema ---
    content += f"class {class_name_base}CreateInSchema({class_name_base}BaseSchema):\n"
    content += f"    id: uuid.UUID | None = Field(None, exclude=True)\n" # Changed to | None
    content += "\n\n"

    # --- <Category>UpdateInSchema ---
    content += f"class {class_name_base}UpdateInSchema({class_name_base}BaseSchema):\n"
    content += f"    id: uuid.UUID | None = Field(None, exclude=True)\n" # Changed to | None
    content += f"    name: str | None = None\n" # Changed to | None
    content += "\n\n"

    # --- <Category>FilterSchema with all foreign key fields ---
    content += f"class {class_name_base}FilterSchema(BaseFilterSchema):\n"
    if filter_schema_fields:
        content += textwrap.indent("\n".join(filter_schema_fields), "    ") + "\n"
    else:
        content += f"    pass # No foreign key fields found\n" # Fallback if no foreign keys
    content += "\n\n"

    # --- <Category>OutSchema ---
    content += f"class {class_name_base}OutSchema(AbstractElementBaseSchema):\n"
    for section, fields in out_schema_fields_dict.items():
         content += f"\n    # {section.capitalize()}\n" # Indented section comment
         content += textwrap.indent("\n".join(fields), "    ") + "\n"
    content += "\n" # Single newline at end of class

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Generated {output_file}")


# --- Main Execution ---
if __name__ == "__main__":
    print("Starting Django Ninja schema generation...")
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Generate base schemas
    base_yaml_path = os.path.join(YAML_SCHEMA_DIR, BASE_PROPERTIES_FILE)
    base_output_path = os.path.join(OUTPUT_DIR, BASE_SCHEMAS_FILENAME)
    generate_base_schemas(base_yaml_path, base_output_path)

    # Generate category schemas
    for filename in os.listdir(YAML_SCHEMA_DIR):
        if filename.endswith('.yaml') and filename != BASE_PROPERTIES_FILE:
            category_name = filename[:-5] # Remove .yaml
            yaml_path = os.path.join(YAML_SCHEMA_DIR, filename)
            output_path = os.path.join(OUTPUT_DIR, f"{category_name}_schemas.py") # Append _schemas here
            generate_category_schema(category_name, yaml_path, output_path)

    print("Schema generation complete.")