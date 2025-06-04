import os
import yaml

def get_django_field_type(yaml_type, field_details=None, model_name=None, is_world=False, is_required=False):
    """Determine Django field type based on YAML type and collect required imports."""
    required_imports = {"models"}
    allow_blank_null = not is_required and not is_world # Required fields or world fields cannot be blank/null

    # Base attributes for fields, adjusted based on whether they are required
    base_attrs = "" if is_required or is_world else ", blank=True, null=True"
    positive_int_attrs = base_attrs
    text_field_attrs = base_attrs
    char_field_attrs = base_attrs
    url_field_attrs = base_attrs
    # Use CASCADE for required FKs, SET_NULL for optional ones
    fk_on_delete = "models.CASCADE" if is_required else "models.SET_NULL" 
    fk_attrs = f", on_delete={fk_on_delete}" + ("" if is_required else ", blank=True, null=True")
    # ManyToManyField allows blank=True even if required conceptually
    m2m_attrs = ", blank=True" 

    if isinstance(yaml_type, dict):
        yaml_type_str = yaml_type.get('type', '')
        if yaml_type_str == 'integer':
            if isinstance(field_details, dict) and 'maximum' in field_details and field_details['maximum'] > 0:
                required_imports.add("validators")
                # Add validators string part, keeping base_attrs
                validators_str = f", validators=[MaxValueValidator({field_details['maximum']})]"
                field_str = f"models.PositiveIntegerField(validators=[MaxValueValidator({field_details['maximum']})]{positive_int_attrs})"
                return field_str, required_imports
            return f"models.PositiveIntegerField({positive_int_attrs.lstrip(', ')})", required_imports
        elif yaml_type_str == 'string':
            return f"models.TextField({text_field_attrs.lstrip(', ')})", required_imports
        elif yaml_type_str == 'multi-link':
            if isinstance(field_details, dict) and 'category' in field_details:
                category = field_details['category']
                field_name = field_details.get('field_name', '')
                related_name = f'"{model_name.lower()}_{field_name}"' if model_name and field_name else None
                related_name_str = f", related_name={related_name}" if related_name else ""
                field_str = f'models.ManyToManyField("{category}"{m2m_attrs}{related_name_str})'
                return field_str, required_imports
            return f'models.ManyToManyField("Element"{m2m_attrs})', required_imports
        elif yaml_type_str == 'single-link':
            if isinstance(field_details, dict) and 'category' in field_details:
                category = field_details['category']
                field_name = field_details.get('field_name', '')
                related_name = f'"{model_name.lower()}_{field_name}"' if model_name and field_name else None
                related_name_str = f", related_name={related_name}" if related_name else ""
                field_str = f'models.ForeignKey("{category}"{fk_attrs}{related_name_str})'
                return field_str, required_imports
            return f'models.ForeignKey("Element"{fk_attrs})', required_imports
        elif yaml_type_str == 'List':
             # JSONField specific default, blank/null handling might differ or be less relevant
            return "models.JSONField(default=list)", required_imports 
        elif yaml_type_str == 'generic-link':
            ct_field_name = 'element_type' # Default
            obj_id_field_name = 'element_id' # Default
            if isinstance(field_details, dict):
                ct_field_name = field_details.get('content_type_field_name', ct_field_name)
                obj_id_field_name = field_details.get('object_id_field_name', obj_id_field_name)

            required_imports.add("contenttypes_fields")
            required_imports.add("contenttypes_models")
            required_imports.add("uuid")
            return ('generic-link', ct_field_name, obj_id_field_name), required_imports
    elif isinstance(yaml_type, str):
        if yaml_type == 'UUID':
            required_imports.add("uuid")
            # Primary key is never blank/null
            return "models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)", required_imports
        elif yaml_type == 'String':
            if isinstance(field_details, dict) and field_details.get('field_name') == 'api_key':
                 # Special case for API key - assuming unique implies non-null/blank
                return "models.CharField(max_length=10, unique=True)", required_imports
            return f"models.CharField(max_length=255{char_field_attrs})", required_imports
        elif yaml_type == 'Integer':
            return f"models.PositiveIntegerField({positive_int_attrs.lstrip(', ')})", required_imports
        elif yaml_type == 'URL':
            return f"models.URLField({url_field_attrs.lstrip(', ')})", required_imports
            
    # Default case
    return f"models.TextField({text_field_attrs.lstrip(', ')})", required_imports

def get_base_field_type(field_name, field_details, is_required=False):
    """Get Django field type for base model fields and collect required imports."""
    field_type = field_details.get('type', 'string')
    description = field_details.get('description', '')
    maximum = field_details.get('maximum')
    required_imports = {"models"}
    
    # Base attributes for fields, adjusted based on whether they are required
    # Used for general fields if not specifically handled below
    base_attrs_nullable = "" if is_required else ", blank=True, null=True"

    # Handle special fields for the base model - ID and Name are inherently required
    if field_name.lower() == 'id':
        required_imports.add("uuid")
        return "models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)", description, required_imports
    elif field_name.lower() == 'name':
        return "models.TextField(max_length=255)", description, required_imports # Always required
    elif field_name.lower() == 'description':
         # Description can be optional unless explicitly required
        return f"models.TextField({base_attrs_nullable.lstrip(', ')})", description, required_imports
    elif field_name.lower() == 'image_url':
         # Image URL can be optional unless explicitly required
        return f"models.URLField({base_attrs_nullable.lstrip(', ')})", description, required_imports
    elif field_name.lower() == 'world':
        # World FK relationship. on_delete=CASCADE makes sense regardless of requirement.
        # Nullability depends on whether 'World' is in the 'required' list in base_properties.yaml
        fk_args = [
            '"worlds.World"',
            'on_delete=models.CASCADE',
            'related_name="%(class)s_related"'
        ]
        if not is_required:
            # Add blank=True, null=True only if World is NOT required
            fk_args.append('blank=True')
            fk_args.append('null=True')

        # Format with newlines for readability
        fk_args_str = f",\n        ".join(fk_args)
        field_string = f'models.ForeignKey(\n        {fk_args_str}\n    )'
        return (field_string, description, required_imports)
    
    # General field type mapping (less likely needed with current base_properties)
    # Use base_attrs_nullable which respects is_required
    if field_type == 'integer':
        if maximum:
            required_imports.add("validators")
            validators_str = f", validators=[MaxValueValidator({maximum})]"
            # Assuming base integer fields are nullable unless required
            return f"models.PositiveIntegerField(validators=[MaxValueValidator({maximum})]{base_attrs_nullable})", description, required_imports
        return f"models.IntegerField({base_attrs_nullable.lstrip(', ')})", description, required_imports
    elif field_type == 'string':
        # Assuming base string fields are nullable unless required
        return f"models.CharField(max_length=255{base_attrs_nullable})", description, required_imports
    else:
         # Default to nullable TextField unless required
        return f"models.TextField({base_attrs_nullable.lstrip(', ')})", description, required_imports

def generate_abstract_element_model(base_properties_path, django_path):
    """Generate abstract base model for all element types."""
    required_imports = {"models"}
    model_content = "class AbstractElementModel(models.Model):\n"
    
    # Load base properties
    with open(base_properties_path, 'r') as file:
        base_yaml = yaml.safe_load(file)
        base_properties = base_yaml.get('properties', {})
        required_base_fields = base_yaml.get('required', []) # Read top-level required fields
    
    # Add fields from base properties
    for field, details in base_properties.items():
        is_required = field in required_base_fields
        # Pass is_required status to base field type getter
        field_type, _, imports = get_base_field_type(field, details, is_required=is_required) 
        required_imports.update(imports)
        model_content += f"    {field.lower()} = {field_type}\n"
    
    # Add Meta class
    model_content += "\n    class Meta:\n"
    model_content += "        abstract = True\n"
        
    # Write the file with imports
    write_django_file(os.path.dirname(django_path), os.path.basename(django_path), model_content, required_imports, "AbstractElementModel", is_world=False, is_abstract=True)

def get_world_django_field_string(field_name, field_details):
    """Generate the specific Django field string for a World model field based on YAML details."""
    field_type = field_details.get('type', 'string')
    field_format = field_details.get('format')
    default = field_details.get('default')
    max_length = field_details.get('maxLength')
    imports = {"models"} # Base import

    if field_name == 'id':
        imports.add("uuid")
        return "models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)", imports
    elif field_name == 'api_key':
        # Use maxLength from schema, default to 10 if not specified
        length = max_length if max_length is not None else 10
        return f"models.CharField(max_length={length}, unique=True)", imports
    elif field_name == 'name':
        return "models.CharField(max_length=255)", imports
    elif field_name == 'description':
        return "models.TextField(blank=True, null=True)", imports
    elif field_name == 'version':
        # Use default from schema, fallback if not present
        default_val = default if default is not None else '0.00.00' # Default specified in your example
        return f"models.CharField(max_length=50, default='{default_val}')", imports
    elif field_name == 'image_url':
        return "models.URLField(blank=True, null=True)", imports
    elif field_name == 'user':
        imports.add("settings")
        return 'models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="worlds")', imports
    elif field_type == 'array':
        imports.add("JSONField")
        # Assuming all array types map to JSONField(default=list) for World
        return "JSONField(default=list)", imports
    elif field_name == 'time_basic_unit':
        default_val = default if default is not None else 'Year'
        return f"models.CharField(max_length=50, default='{default_val}')", imports
    elif field_name in ['time_range_min', 'time_range_max', 'time_current']:
        # Use default from schema, provide fallback if needed
        default_val = default if default is not None else 0
        # Ensure default is treated as integer for PositiveIntegerField
        return f"models.PositiveIntegerField(default={int(default_val)})", imports
    else:
        # Fallback for any unexpected fields in world.yaml
        # print(f"Warning: Unhandled field '{field_name}' in World schema. Defaulting to TextField.")
        return "models.TextField(blank=True, null=True)", imports

def extract_fields(yaml_data, class_name=None, is_world=False):
    """Extract field definitions from YAML data and collect required imports.
    The required_imports set tracks strings needed for the *output file*.
    """
    fields = []
    required_imports = {"models"} # Default needed for models.Model etc.

    if is_world:
        world_props = yaml_data.get('properties', {})
        temp_fields = {}
        for field_name, field_details in world_props.items():
            # Use the new helper function to get the exact string and imports
            field_string, imports = get_world_django_field_string(field_name, field_details)
            temp_fields[field_name] = field_string
            required_imports.update(imports)

        # Reorder fields to match the desired model structure
        ordered_fields = []
        field_order = [
            'id', 'api_key', 'name', 'description', 'version', 'image_url',
            'time_format_equivalents', 'time_format_names', 'time_basic_unit',
            'time_range_min', 'time_range_max', 'time_current', 'user'
        ]
        for field_name in field_order:
            if field_name in temp_fields:
                ordered_fields.append((field_name, temp_fields[field_name]))
        # Add any fields from YAML not in the predefined order (for robustness)
        for field_name, field_string in temp_fields.items():
            if field_name not in field_order:
                # print(f"Warning: Field '{field_name}' found in world.yaml but not in expected order.")
                ordered_fields.append((field_name, field_string))
        fields = ordered_fields

    # Existing logic for non-world elements
    elif 'properties' in yaml_data:
        top_level_properties = yaml_data['properties']
        top_level_required = yaml_data.get('required', []) # Get top-level required list

        for section, section_data in top_level_properties.items():
            section_fields = []
            # Check if this section represents a nested object
            if isinstance(section_data, dict) and section_data.get('type') == 'object' and 'properties' in section_data:
                nested_properties = section_data['properties']
                nested_required = section_data.get('required', []) # Required fields *within* this section

                for field, field_details in nested_properties.items():
                    if isinstance(field_details, dict):
                        field_details['field_name'] = field # Pass field name for context

                    is_field_required = field in nested_required
                    # Use the original get_django_field_type for non-world elements
                    django_field, imports = get_django_field_type(
                        field_details, field_details, class_name, is_world=False, is_required=is_field_required
                    )
                    required_imports.update(imports)
                    section_fields.append((field, django_field))

            if section_fields:
                fields.append((section, section_fields))

    return fields, required_imports

def generate_django_model(class_name, fields, required_imports, is_world=False):
    """Generate Django model class string from field definitions."""
    base_class = 'models.Model' if is_world else 'AbstractElementModel'
    model = f"class {class_name}({base_class}):\n"

    if is_world:
        model += "    objects = models.Manager()\n"
        for field, field_type_str in fields:
            model += f"    {field} = {field_type_str}\n"
    else: # Standard element model generation (including those with generic links)
        # Ensure UUID import if needed by generic link fields
        if any(isinstance(ft, tuple) and ft[0] == 'generic-link' for _, s_fields in fields for _, ft in s_fields):
            required_imports.add("uuid")
            required_imports.add("contenttypes_fields")
            required_imports.add("contenttypes_models")

        for section_name, section_fields in fields:
            model += f"\n    # {section_name.capitalize()}\n"
            for field, field_type in section_fields:
                # Check if it's the special marker for a generic link
                if isinstance(field_type, tuple) and field_type[0] == 'generic-link':
                    ct_name = field_type[1]
                    obj_name = field_type[2]
                    # Add the three fields for the GenericForeignKey relationship
                    model += f"    {ct_name} = models.ForeignKey(ContentType, on_delete=models.CASCADE, blank=True, null=True)\n"
                    model += f"    {obj_name} = models.UUIDField(blank=True, null=True)\n"
                    model += f"    {field} = GenericForeignKey('{ct_name}', '{obj_name}')\n"
                else:
                    # Generate standard field
                    model += f"    {field} = {field_type}\n"

    model += "\n    def __str__(self):\n"
    model += "        return self.name\n"

    return model, required_imports

def generate_import_statements(required_imports, class_name, is_world, is_abstract=False):
    """Generate import statement strings based on collected requirements for the output file."""
    import_lines = []
    # Map the collected strings to actual import statements
    if "models" in required_imports:
        import_lines.append("from django.db import models")
    if "uuid" in required_imports:
        import_lines.append("import uuid")
    if "validators" in required_imports:
        import_lines.append("from django.core.validators import MaxValueValidator")
    # Use distinct keys for GFK imports to avoid ambiguity
    if "contenttypes_fields" in required_imports:
        import_lines.append("from django.contrib.contenttypes.fields import GenericForeignKey")
    if "contenttypes_models" in required_imports:
        import_lines.append("from django.contrib.contenttypes.models import ContentType")
    if "settings" in required_imports:
        import_lines.append("from django.conf import settings")
    if "JSONField" in required_imports:
        import_lines.append("from django.db.models import JSONField")

    # Add base model import string unless it's the abstract model itself
    if not is_abstract:
        if is_world:
            # World inherits directly from models.Model
            pass
        else:
            # All other elements inherit from AbstractElementModel
            import_lines.append(f"from .abstract_element_model import AbstractElementModel")

    # Sort for consistency and add newlines
    return "\n".join(sorted(list(set(import_lines)))) + "\n\n" if import_lines else ""


def write_django_file(directory, filename, model_content, required_imports, class_name, is_world, is_abstract=False):
    """Write content to a file, prepending necessary imports."""
    import_statements = generate_import_statements(required_imports, class_name, is_world, is_abstract)
    full_content = import_statements + model_content
    
    with open(os.path.join(directory, filename), 'w') as file:
        file.write(full_content)

def convert_yaml_to_django(yaml_path, django_path):
    """Convert YAML file to Django model."""
    with open(yaml_path, 'r') as yaml_file:
        yaml_content = yaml.safe_load(yaml_file)
    
    filename = os.path.basename(yaml_path)
    class_name = filename.replace('.yaml', '').capitalize()
    is_world = class_name == 'World'
    
    fields, required_imports = extract_fields(yaml_content, class_name, is_world)
    django_model, final_imports = generate_django_model(class_name, fields, required_imports, is_world)
    
    output_filename = f"{filename.replace('.yaml', '')}.py"
    write_django_file(django_path, output_filename, django_model, final_imports, class_name, is_world)
    print(f"Generated Django model for {class_name} in {output_filename}")

if __name__ == "__main__":
    script_directory = os.path.dirname(__file__)
    yaml_dir = os.path.join(script_directory, '..', 'schema')
    django_dir = os.path.join(script_directory, '..', 'languages', 'django_models')
    base_path = os.path.join(yaml_dir, 'base_properties.yaml')
    
    os.makedirs(django_dir, exist_ok=True)
    
    # Generate the abstract element model
    abstract_model_path = os.path.join(django_dir, 'abstract_element_model.py')
    generate_abstract_element_model(base_path, abstract_model_path)
    print(f"Generated abstract element model: abstract_element_model.py")
    
    # Generate models for all schema files
    for filename in os.listdir(yaml_dir):
        if filename.endswith('.yaml') and filename != 'base_properties.yaml':
            yaml_path = os.path.join(yaml_dir, filename)
            convert_yaml_to_django(yaml_path, django_dir)
