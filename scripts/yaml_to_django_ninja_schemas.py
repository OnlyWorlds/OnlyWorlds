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
       Context can be 'base' or 'out'.
    """
    yaml_type = yaml_type_details.get('type') if isinstance(yaml_type_details, dict) else yaml_type_details

    if not yaml_type:
        return "Any | None"

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
            return "uuid.UUID | None" # Use UUID directly for base/input IDs
        elif yaml_type == 'multi-link':
            return "list[uuid.UUID] | None" # Use list[uuid.UUID] for base/input IDs
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
         # Add other non-link types if needed for Out context specifically
         else: # Fallback for non-link types in Out context
             return get_python_type_hint(yaml_type_details, context="base")

    # Fallback for simple types defined directly (like in base_properties)
    if isinstance(yaml_type, str):
        if yaml_type.lower() == 'string': return "str | None"
        if yaml_type.lower() == 'integer': return "int | None"
        if yaml_type.lower() == 'url': return "str | None"
        if yaml_type.lower() == 'uuid': return "uuid.UUID"

    return "Any | None"

def generate_field_definition(field_name, yaml_details, imports_tracker, context="base"):
    """Generates a Ninja schema field definition string."""
    py_type_hint = get_python_type_hint(yaml_details, context=context)
    py_field_name = field_name

    field_args = []
    default_value = "None"

    # Handle reserved keywords - use trailing underscore convention
    if keyword.iskeyword(field_name):
        py_field_name = f"{field_name}_"
        field_args.append(f"alias='{field_name}'")
        imports_tracker['Field'] = "from ninja import Field" # Ensure Field is imported

    # Handle constraints (only 'maximum' for 'le' currently)
    maximum = yaml_details.get('maximum') if isinstance(yaml_details, dict) else None
    if maximum is not None and isinstance(maximum, (int, float)) and maximum > 0:
        # Don't add default_value=None to Field args if we already have constraints
        constraint_args = [f"le={maximum}"]
        field_args.extend(constraint_args)
        imports_tracker['Field'] = "from ninja import Field" # Ensure Field is imported

    # Build Field string if needed
    if field_args:
        # Add default 'None' as first arg for Field(...) unless type doesn't include '| None'
        field_content = [default_value] + field_args if "| None" in py_type_hint else field_args
        field_args_str = ", ".join(field_content)
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
        from typing import Optional
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
    content += "    name__icontains: Optional[str] = Field(None, q='name__icontains')\n"
    content += "    supertype: Optional[str] = Field(None, q='supertype')\n"
    content += "    subtype: Optional[str] = Field(None, q='subtype')\n"

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
        'typing_Optional': "from typing import Optional",
        'uuid': "import uuid"
    }
    # Track which specific imports are actually used by the fields generated
    imports_tracker = defaultdict(bool)
    imports_tracker['base'] = True # Always needed
    imports_tracker['ninja'] = True # Assume always needed
    imports_tracker['uuid'] = True # Assume always needed
    imports_tracker['typing_Optional'] = True # Likely needed for | None or Optional[]

    base_schema_fields_dict = defaultdict(list)
    out_schema_fields_dict = defaultdict(list)
    filter_schema_fields = []

    # Process fields and group by section
    for section, section_data in category_yaml.get('properties', {}).items():
        if isinstance(section_data, dict) and 'properties' in section_data:
            for field, details in section_data['properties'].items():
                # --- Field for Base Schema ---
                # Use the raw field name (e.g., 'species', 'birthplace')
                field_def_base = generate_field_definition(field, details, imports_tracker, context="base")
                base_schema_fields_dict[section].append(field_def_base)
                if 'list[' in field_def_base: imports_tracker['typing_list_primitive'] = True # Track primitive list usage
                if 'uuid.UUID' in field_def_base: imports_tracker['uuid'] = True

                # --- Field for Out Schema ---
                yaml_link_type = details.get('type') if isinstance(details, dict) else None
                out_field_name = get_nested_out_field_name(field, yaml_link_type)

                if yaml_link_type == 'single-link':
                    out_schema_fields_dict[section].append(f"{out_field_name}: Optional[ElementNestedOutSchema] = None")
                    imports_tracker['typing_Optional'] = True
                    # Add filter field for single-link
                    filter_schema_fields.append(f"{field}_id: Optional[uuid.UUID] = Field(None, q='{field}_id')")
                elif yaml_link_type == 'multi-link':
                    out_schema_fields_dict[section].append(f"{out_field_name}: List[ElementNestedOutSchema] = []")
                    imports_tracker['typing_List'] = True # Track usage of typing.List
                    # Add filter field for multi-link
                    filter_schema_fields.append(f"{field}_ids: Optional[uuid.UUID] = Field(None, q='{field}__id')")
                else:
                    # Regular field, potentially with constraints for Out schema too
                    field_def_out = generate_field_definition(field, details, imports_tracker, context="out")
                    out_schema_fields_dict[section].append(field_def_out)

    # Build import string based on tracked usage
    final_import_lines = [imports_needed['base']]
    if imports_tracker['ninja']: final_import_lines.append(imports_needed['ninja'])
    # Combine List/Optional imports if both needed
    typing_imports = []
    if imports_tracker['typing_List']: typing_imports.append("List")
    if imports_tracker['typing_Optional']: typing_imports.append("Optional")
    if typing_imports:
        final_import_lines.append(f"from typing import {', '.join(typing_imports)}")
    elif imports_tracker['typing_list_primitive']: # If only primitive list used
         final_import_lines.append("from typing import List") # Or just keep Optional? Target uses list[]

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
    content += f"    id: Optional[uuid.UUID] = Field(None, exclude=True)\n"
    content += "\n\n"

    # --- <Category>UpdateInSchema ---
    content += f"class {class_name_base}UpdateInSchema({class_name_base}BaseSchema):\n"
    content += f"    id: Optional[uuid.UUID] = Field(None, exclude=True)\n"
    content += f"    name: Optional[str] = None\n"
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