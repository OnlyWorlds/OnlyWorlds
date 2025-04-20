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

def get_python_type_hint(yaml_type_details, context="base"):
    """Maps YAML type details to Python type hints for Ninja schemas.
       Uses `| None` instead of `Optional`. Context can be 'base' or 'out'.
    """
    yaml_type = yaml_type_details.get('type') if isinstance(yaml_type_details, dict) else yaml_type_details

    if not yaml_type:
        return "Any | None" # Keep Any | None as it's not Optional[Any]

    # Types for Base/In/Update Schemas
    if context == "base":
        if yaml_type == 'string':
            return "str | None"
        elif yaml_type == 'integer':
            return "int | None"
        elif yaml_type == 'boolean':
            return "bool | None"
        elif yaml_type == 'number':
            return "float | None"
        elif yaml_type == 'single-link':
            return "uuid.UUID | None"
        elif yaml_type == 'multi-link':
            return "list[uuid.UUID] | None"
        elif yaml_type == 'array':
            item_type_hint = get_python_type_hint(yaml_type_details.get('items', {'type': 'string'}), context)
            item_type_base = item_type_hint.replace(" | None", "")
            return f"list[{item_type_base}] | None"

    # Types for Out Schemas (handled in generate_category_schema)
    elif context == "out":
         if yaml_type == 'string':
            return "str | None"
         elif yaml_type == 'integer':
            return "int | None"
         elif yaml_type == 'boolean':
            return "bool | None"
         elif yaml_type == 'number':
            return "float | None"
         # Add other non-link types if needed for Out context specifically
         else: # Fallback for non-link types in Out context
             return get_python_type_hint(yaml_type_details, context="base")

    # Fallback for simple types defined directly (like in base_properties)
    if isinstance(yaml_type, str):
        if yaml_type.lower() == 'string': return "str | None"
        if yaml_type.lower() == 'integer': return "int | None"
        if yaml_type.lower() == 'url': return "str | None"
        if yaml_type.lower() == 'uuid': return "uuid.UUID" # UUID itself is not optional here

    return "Any | None" # Default fallback

def generate_field_definition(field_name, yaml_details, imports_tracker, context="base", alias=None):
    """Generates a Ninja schema field definition string."""
    py_type_hint = get_python_type_hint(yaml_details, context=context)
    py_field_name = field_name # Use the name passed in

    field_args = []
    # Determine default value based on type hint and context
    if context == 'out' and py_type_hint.startswith('List['):
        default_value = "[]"
    else:
        default_value = "None"

    # Handle explicit alias first (usually for base properties like Image_URL)
    # We will NOT add aliases for keywords here anymore, that's handled by renaming.
    if alias:
        field_args.append(f"alias='{alias}'")
        imports_tracker['Field'] = "from ninja import Field"

    # Handle constraints (only 'maximum' for 'le' currently)
    maximum = yaml_details.get('maximum') if isinstance(yaml_details, dict) else None
    if maximum is not None and isinstance(maximum, (int, float)) and maximum > 0:
        constraint_args = [f"le={maximum}"]
        if field_args: # Already using Field(...) for alias
             field_args.extend(constraint_args)
        # If not using Field for alias, check if default needed
        elif "| None" in py_type_hint or default_value == "None":
             field_args = [default_value] + constraint_args
        else: # Type is not optional (e.g., List) or default is []
             field_args = constraint_args
        imports_tracker['Field'] = "from ninja import Field"

    # Build Field string if needed
    if field_args:
        # Check if default 'None' should be the first arg (if not already added by constraints)
        final_field_args = field_args
        if default_value == "None" and ("| None" in py_type_hint or "ElementNestedOutSchema | None" in py_type_hint) and (not final_field_args or default_value not in final_field_args[0]):
             final_field_args.insert(0, default_value)

        field_args_str = ", ".join(final_field_args)
        return f"{py_field_name}: {py_type_hint} = Field({field_args_str})"
    else:
        # Simple assignment if no Field args
        return f"{py_field_name}: {py_type_hint} = {default_value}"


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
    imports_tracker = defaultdict(str) # Track needed imports like Field

    # Generate AbstractElementBaseSchema
    for field, details in base_properties.items():
        py_field_name = field.lower()
        py_type_hint = get_python_type_hint(details)
        field_def = f"{py_field_name}: {py_type_hint}"

        if py_field_name == 'id':
            field_def = f"id: uuid.UUID"
        elif py_field_name == 'name':
             field_def = f"name: str"
        elif py_field_name == 'world':
             field_def = f"world: uuid.UUID | None = None"
        elif field != py_field_name: # Original name differs (e.g., Image_URL)
             field_def += f" = Field(None, alias='{field}')"
             imports_tracker['Field'] = "from ninja import Field" # Ensure Field imported
        else:
            field_def += " = None"

        base_fields.append(field_def)

        # Define fields for NestedOutSchema based on target file
        if py_field_name in ['id', 'name', 'supertype', 'subtype', 'image_url']:
             if py_field_name == 'id':
                 nested_out_fields.append(f"id: uuid.UUID")
             elif py_field_name == 'name':
                 nested_out_fields.append(f"name: str")
             elif py_field_name == 'image_url' and field != py_field_name:
                 nested_out_fields.append(f"{py_field_name}: str | None = Field(None, alias='{field}')")
                 imports_tracker['Field'] = "from ninja import Field"
             else:
                 nested_out_fields.append(f"{py_field_name}: str | None = None")


    # Ensure Field import is added if used
    if 'Field' in imports_tracker and 'Field' not in imports_content:
         # This logic might need refinement based on final import structure
         pass # Assuming Field is included in the initial import block

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
            for field, details in section_data['properties'].items():
                yaml_link_type = details.get('type') if isinstance(details, dict) else None
                original_field_name = field

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


                # --- Field for Base Schema ---
                # Generate using the final base schema name (_id/_ids included)
                # Pass alias ONLY if explicitly needed (e.g. Image_URL, not for keywords)
                field_def_base = generate_field_definition(
                    py_final_schema_name_for_base, details, imports_tracker, context="base", alias=py_explicit_alias_for_base
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