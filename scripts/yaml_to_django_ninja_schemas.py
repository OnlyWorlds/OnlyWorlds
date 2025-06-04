import os
import yaml
import keyword
import textwrap
from collections import defaultdict

YAML_SCHEMA_DIR = os.path.join(os.path.dirname(__file__), '..', 'schema')
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'languages', 'django_ninja_schemas')
BASE_PROPERTIES_FILE = 'base_properties.yaml'
BASE_SCHEMAS_FILENAME = 'base_schemas.py'

def safe_load_yaml(filepath):
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
    yaml_type = yaml_type_details.get('type') if isinstance(yaml_type_details, dict) else yaml_type_details

    if not yaml_type:
        return "Any" if is_required else "Any | None"

    optional_suffix = "" if is_required else " | None"

    if context in ["base", "in", "update"]:
        if yaml_type == 'string': return f"str{optional_suffix}"
        if yaml_type == 'integer': return f"int{optional_suffix}"
        if yaml_type == 'boolean': return f"bool{optional_suffix}"
        if yaml_type == 'number': return f"float{optional_suffix}"
        if yaml_type == 'single-link': return f"uuid.UUID{optional_suffix}"
        if yaml_type == 'multi-link': return f"list[uuid.UUID]{optional_suffix}"
        if yaml_type == 'generic-link': return "handled_by_generic_link"
        if yaml_type == 'array':
            items = yaml_type_details.get('items', {'type': 'any'})
            item_type_hint = get_python_type_hint(items, context='base', is_required=False)
            item_type_base = item_type_hint.replace(" | None", "")
            if items.get('type') == 'string' and is_required:
                return f"List[str]"
            return f"list[{item_type_base}]{optional_suffix}"
        if yaml_type == 'url': return f"str{optional_suffix}"

    elif context == "out":
        if yaml_type == 'string': return f"str{optional_suffix}"
        if yaml_type == 'integer': return f"int{optional_suffix}"
        if yaml_type == 'boolean': return f"bool{optional_suffix}"
        if yaml_type == 'number': return f"float{optional_suffix}"
        if yaml_type == 'array':
            items = yaml_type_details.get('items', {'type': 'any'})
            item_type_hint = get_python_type_hint(items, context='base', is_required=False)
            item_type_base = item_type_hint.replace(" | None", "")
            return f"list[{item_type_base}]{optional_suffix}"
        if yaml_type == 'url': return f"str{optional_suffix}"

    if isinstance(yaml_type, str):
        simple_optional_suffix = "" if is_required else " | None"
        if yaml_type.lower() == 'string': return f"str{simple_optional_suffix}"
        if yaml_type.lower() == 'integer': return f"int{simple_optional_suffix}"
        if yaml_type.lower() == 'url': return f"str{simple_optional_suffix}"
        if yaml_type.lower() == 'uuid': return "uuid.UUID"

    return "Any" if is_required else "Any | None"

def generate_field_definition(field_name, yaml_details, imports_tracker, context="base", alias=None, is_required=False):
    yaml_type = yaml_details.get('type') if isinstance(yaml_details, dict) else None

    if yaml_type == 'generic-link' and context == 'base':
        ct_field_name = yaml_details.get('content_type_field_name', 'content_type')
        obj_id_field_name = yaml_details.get('object_id_field_name', 'object_id')
        ct_py_type = "str" if is_required else "str | None"
        obj_py_type = "uuid.UUID" if is_required else "uuid.UUID | None"
        default_assignment = "" if is_required else " = None"
        imports_tracker['uuid'] = True
        ct_def = f"{ct_field_name}: {ct_py_type}{default_assignment}"
        obj_id_def = f"{obj_id_field_name}: {obj_py_type}{default_assignment}"
        return [ct_def, obj_id_def]

    py_type_hint = get_python_type_hint(yaml_details, context=context, is_required=is_required)

    if py_type_hint == "handled_by_generic_link":
        print(f"Warning: generate_field_definition called unexpectedly for generic-link field '{field_name}' in context '{context}'")
        return []
    if "List[" in py_type_hint: imports_tracker['typing_List'] = True
    if "uuid.UUID" in py_type_hint: imports_tracker['uuid'] = True

    py_field_name = field_name
    field_args = []
    field_args_str = ""
    default_assignment = ""

    if not is_required:
        if py_type_hint.startswith('list[') or py_type_hint == "List[str]":
             default_assignment = " = None"
             imports_tracker['typing_List'] = True
        elif " | None" in py_type_hint:
            default_assignment = " = None"

    if alias:
        field_args.append(f"alias='{alias}'")
        imports_tracker['Field'] = True

    maximum = yaml_details.get('maximum') if isinstance(yaml_details, dict) else None
    if maximum is not None and isinstance(maximum, (int, float)) and maximum > 0:
        constraint_args = [f"le={maximum}"]
        if not is_required:
            field_args = ["None"] + constraint_args
        else:
             field_args = constraint_args
        imports_tracker['Field'] = True

    if field_args:
        if not is_required and (not field_args or "None" not in field_args[0]):
            if "None" not in field_args: field_args.insert(0, "None")
        field_args_str = ", ".join(field_args)
        assignment_part = f" = Field({field_args_str})"
        return [f"{py_field_name}: {py_type_hint}{assignment_part}"]
    else:
        assign = default_assignment if not is_required else ""
        return [f"{py_field_name}: {py_type_hint}{assign}"]

def generate_category_schema(category_name, category_yaml_path, output_file):
    category_yaml = safe_load_yaml(category_yaml_path)
    if not category_yaml or 'properties' not in category_yaml:
        print(f"Warning: Skipping {category_name}. Could not load or parse YAML.")
        return

    class_name_base = category_name.capitalize()

    imports_needed = {
        'base': f"from .base_schemas import AbstractElementBaseSchema, ElementNestedOutSchema, BaseFilterSchema",
        'ninja': "from ninja import Field # type: ignore",
        'typing_List': "from typing import List",
        'uuid': "import uuid"
    }
    imports_tracker = defaultdict(bool)
    imports_tracker['base'] = True
    imports_tracker['ninja'] = True
    imports_tracker['uuid'] = True

    base_schema_fields_dict = defaultdict(list)
    out_schema_fields_dict = defaultdict(list)
    filter_schema_fields = []

    for section, section_data in category_yaml.get('properties', {}).items():
        if isinstance(section_data, dict) and 'properties' in section_data:
            nested_properties = section_data['properties']
            nested_required = section_data.get('required', [])

            for field, details in nested_properties.items():
                original_field_name = field
                is_field_required = original_field_name in nested_required
                yaml_link_type = details.get('type') if isinstance(details, dict) else None

                py_schema_name = original_field_name
                py_explicit_alias_for_base = None
                if keyword.iskeyword(original_field_name):
                    py_schema_name = f"{category_name.lower()}_{original_field_name}"

                py_schema_name_for_base_link = py_schema_name
                if yaml_link_type == 'single-link': py_schema_name_for_base_link = f"{py_schema_name}_id"
                elif yaml_link_type == 'multi-link': py_schema_name_for_base_link = f"{py_schema_name}_ids"

                py_final_schema_name_for_out = py_schema_name

                field_defs_base = generate_field_definition(
                    py_schema_name_for_base_link if yaml_link_type in ['single-link', 'multi-link'] else original_field_name,
                    details, imports_tracker, context="base",
                    alias=py_explicit_alias_for_base,
                    is_required=is_field_required
                )
                base_schema_fields_dict[section].extend(field_defs_base)

                if yaml_link_type == 'single-link':
                    nested_type = "ElementNestedOutSchema"
                    type_hint = f"{nested_type}" if is_field_required else f"{nested_type} | None"
                    default = "" if is_field_required else " = None"
                    out_schema_fields_dict[section].append(f"{py_final_schema_name_for_out}: {type_hint}{default}")
                elif yaml_link_type == 'multi-link':
                    nested_type = "ElementNestedOutSchema"
                    out_schema_fields_dict[section].append(f"{py_final_schema_name_for_out}: List[{nested_type}] = []")
                    imports_tracker['typing_List'] = True
                elif yaml_link_type == 'generic-link':
                    ct_field_name = details.get('content_type_field_name', 'content_type')
                    obj_id_field_name = details.get('object_id_field_name', 'object_id')
                    ct_type = "str" if is_field_required else "str | None"
                    obj_type = "uuid.UUID" if is_field_required else "uuid.UUID | None"
                    default_assignment = "" if is_field_required else " = None"
                    out_schema_fields_dict[section].append(f"{ct_field_name}: {ct_type}{default_assignment}")
                    out_schema_fields_dict[section].append(f"{obj_id_field_name}: {obj_type}{default_assignment}")
                    imports_tracker['uuid'] = True
                else:
                    field_defs_out = generate_field_definition(
                        py_final_schema_name_for_out,
                        details, imports_tracker, context="out",
                        alias=py_explicit_alias_for_base,
                        is_required=is_field_required
                    )
                    out_schema_fields_dict[section].extend(field_defs_out)

                if yaml_link_type == 'single-link':
                    filter_field_name = f"{py_schema_name_for_base_link}"
                    q_lookup = filter_field_name
                    filter_schema_fields.append(f"{filter_field_name}: uuid.UUID | None = Field(None, q='{q_lookup}')")
                    imports_tracker['Field'] = True
                    imports_tracker['uuid'] = True
                elif yaml_link_type == 'multi-link':
                    filter_field_name = f"{py_schema_name_for_base_link}"
                    q_lookup = f'{original_field_name}__id'
                    filter_schema_fields.append(f"{filter_field_name}: uuid.UUID | None = Field(None, q='{q_lookup}')")
                    imports_tracker['Field'] = True
                    imports_tracker['uuid'] = True

    final_import_lines = []
    if imports_tracker['base']: final_import_lines.append(imports_needed['base'])
    if imports_tracker['Field'] or filter_schema_fields:
        final_import_lines.append(imports_needed['ninja'])
    typing_imports = []
    if imports_tracker['typing_List']: typing_imports.append("List")
    if typing_imports: final_import_lines.append(f"from typing import {', '.join(typing_imports)}")
    if imports_tracker['uuid']: final_import_lines.append(imports_needed['uuid'])
    content = "\n".join(final_import_lines) + "\n\n\n"

    content += f"class {class_name_base}BaseSchema(AbstractElementBaseSchema):\n"
    added_base_fields = False
    for section, fields in base_schema_fields_dict.items():
        if fields:
            content += f"\n    # {section.capitalize()}\n"
            content += textwrap.indent("\n".join(fields), "    ") + "\n"
            added_base_fields = True
    if not added_base_fields:
        content += "    pass\n"
    content += "\n\n"

    content += f"class {class_name_base}CreateInSchema({class_name_base}BaseSchema):\n"
    content += "    id: uuid.UUID | None = Field(None, exclude=True)\n"
    content += "\n\n"

    content += f"class {class_name_base}UpdateInSchema({class_name_base}BaseSchema):\n"
    content += "    id: uuid.UUID | None = Field(None, exclude=True)\n"
    content += "    name: str | None = None\n"
    for section, fields in base_schema_fields_dict.items():
         for field_def in fields:
             field_name = field_def.split(":")[0].strip()
             if field_name not in ['id', 'name']:
                 pass
    if imports_tracker['Field']: imports_tracker['ninja'] = True
    content += "\n\n"

    content += f"class {class_name_base}FilterSchema(BaseFilterSchema):\n"
    if filter_schema_fields:
        content += textwrap.indent("\n".join(filter_schema_fields), "    ") + "\n"
        if imports_tracker['Field']: imports_tracker['ninja'] = True
    else:
        content += "    pass\n"
    content += "\n\n"

    content += f"class {class_name_base}OutSchema(AbstractElementBaseSchema):\n"
    added_out_fields = False
    for section, fields in out_schema_fields_dict.items():
        if fields:
            content += f"\n    # {section.capitalize()}\n"
            content += textwrap.indent("\n".join(fields), "    ") + "\n"
            added_out_fields = True
    if not added_out_fields:
        content += "    pass\n"
    content += "\n"

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Generated {output_file}")

if __name__ == "__main__":
    print("Starting Django Ninja schema generation...")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"Skipping base schema generation for now to focus on category: {BASE_SCHEMAS_FILENAME}")
    for filename in os.listdir(YAML_SCHEMA_DIR):
        if filename.endswith('.yaml') and filename != BASE_PROPERTIES_FILE:
            category_name = filename[:-5]
            yaml_path = os.path.join(YAML_SCHEMA_DIR, filename)
            output_path = os.path.join(OUTPUT_DIR, f"{category_name}_schemas.py")
            if category_name == 'world':
                print(f"Skipping hardcoded world schema generation: {output_path}")
            else:
                generate_category_schema(category_name, yaml_path, output_path)
    print("Schema generation complete.")