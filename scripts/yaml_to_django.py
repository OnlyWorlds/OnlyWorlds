import os
import yaml
from collections import defaultdict
 

def get_django_field_type(yaml_type, field_details=None, model_name=None, is_world=False):
    """Determine Django field type based on YAML type and collect required imports."""
    required_imports = {"models"}
    
    if isinstance(yaml_type, dict):
        yaml_type_str = yaml_type.get('type', '')
        if yaml_type_str == 'integer':
            if isinstance(field_details, dict) and 'maximum' in field_details and field_details['maximum'] > 0:
                required_imports.add("validators")
                field_str = f"models.PositiveIntegerField(blank=True, null=True, validators=[MaxValueValidator({field_details['maximum']})])" if not is_world else f"models.PositiveIntegerField(validators=[MaxValueValidator({field_details['maximum']})])"
                return field_str, required_imports
            return "models.PositiveIntegerField(blank=True, null=True)" if not is_world else "models.PositiveIntegerField()", required_imports
        elif yaml_type_str == 'string':
            return "models.TextField(blank=True, null=True)" if not is_world else "models.TextField()", required_imports
        elif yaml_type_str == 'multi-link':
            if isinstance(field_details, dict) and 'category' in field_details:
                category = field_details['category']
                field_name = field_details.get('field_name', '')
                related_name = f'"{model_name.lower()}_{field_name}"' if model_name and field_name else None
                field_str = f'models.ManyToManyField("{category}", blank=True, related_name={related_name})' if related_name else f'models.ManyToManyField("{category}", blank=True)'
                return field_str, required_imports
            return 'models.ManyToManyField("Element", blank=True)', required_imports
        elif yaml_type_str == 'single-link':
            if isinstance(field_details, dict) and 'category' in field_details:
                category = field_details['category']
                field_name = field_details.get('field_name', '')
                related_name = f'"{model_name.lower()}_{field_name}"' if model_name and field_name else None
                field_str = f'models.ForeignKey("{category}", on_delete=models.SET_NULL, blank=True, null=True, related_name={related_name})' if related_name else f'models.ForeignKey("{category}", on_delete=models.SET_NULL, blank=True, null=True)'
                return field_str, required_imports
            return 'models.ForeignKey("Element", on_delete=models.SET_NULL, blank=True, null=True)', required_imports
        elif yaml_type_str == 'List':
            return "models.JSONField(default=list)", required_imports
    elif isinstance(yaml_type, str):
        if yaml_type == 'UUID':
            required_imports.add("uuid")
            return "models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)", required_imports
        elif yaml_type == 'String':
            if isinstance(field_details, dict) and field_details.get('field_name') == 'api_key':
                return "models.CharField(max_length=10, unique=True)", required_imports
            return "models.CharField(max_length=255, blank=True, null=True)" if not is_world else "models.CharField(max_length=255)", required_imports
        elif yaml_type == 'Integer':
            return "models.PositiveIntegerField(blank=True, null=True)" if not is_world else "models.PositiveIntegerField()", required_imports
        elif yaml_type == 'URL':
            return "models.URLField(blank=True, null=True)", required_imports
            
    # Default case
    return "models.TextField(blank=True, null=True)" if not is_world else "models.TextField()", required_imports

def get_base_field_type(field_name, field_details):
    """Get Django field type for base model fields and collect required imports."""
    field_type = field_details.get('type', 'string')
    description = field_details.get('description', '')
    maximum = field_details.get('maximum')
    required_imports = {"models"}
    
    # Handle special fields for the base model
    if field_name.lower() == 'id':
        required_imports.add("uuid")
        return "models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)", description, required_imports
    elif field_name.lower() == 'name':
        return "models.TextField(max_length=255)", description, required_imports
    elif field_name.lower() == 'description':
        return "models.TextField(blank=True, null=True)", description, required_imports
    elif field_name.lower() == 'image_url':
        return "models.URLField(blank=True, null=True)", description, required_imports
    elif field_name.lower() == 'world':
        # Assuming worlds.World is defined elsewhere and doesn't need a direct import here
        return ('models.ForeignKey(\n        "worlds.World",\n        on_delete=models.CASCADE,'
                '\n        related_name="%(class)s_related",\n    )', description, required_imports)
    
    # General field type mapping
    if field_type == 'integer':
        if maximum:
            required_imports.add("validators")
            return f"models.PositiveIntegerField(blank=True, null=True, validators=[MaxValueValidator({maximum})])", description, required_imports
        return "models.IntegerField(blank=True, null=True)", description, required_imports
    elif field_type == 'string':
        return "models.CharField(max_length=255, blank=True, null=True)", description, required_imports
    else:
        return "models.TextField(blank=True, null=True)", description, required_imports

def generate_abstract_element_model(base_properties_path, django_path):
    """Generate abstract base model for all element types."""
    required_imports = {"models"}
    model_content = "class AbstractElementModel(models.Model):\n"
    
    # Load base properties
    with open(base_properties_path, 'r') as file:
        base_yaml = yaml.safe_load(file)
        base_properties = base_yaml.get('properties', {})
    
    # Add fields from base properties
    for field, details in base_properties.items():
        field_type, _, imports = get_base_field_type(field, details)
        required_imports.update(imports)
        model_content += f"    {field.lower()} = {field_type}\n"
    
    # Add Meta class
    model_content += "\n    class Meta:\n"
    model_content += "        abstract = True\n"
        
    # Write the file with imports
    write_django_file(os.path.dirname(django_path), os.path.basename(django_path), model_content, required_imports, "AbstractElementModel", is_world=False, is_abstract=True)


def extract_fields(yaml_data, class_name=None, is_world=False):
    """Extract field definitions from YAML data and collect required imports."""
    fields = []
    required_imports = set()
    
    if is_world and 'World' in yaml_data:
        for field, field_type in yaml_data['World'].items():
            if isinstance(field_type, dict):
                field_type['field_name'] = field
            django_field, imports = get_django_field_type(field_type, field_type, 'World', is_world=True)
            required_imports.update(imports)
            fields.append((field, django_field))
    elif 'properties' in yaml_data:
        for section, section_data in yaml_data['properties'].items():
            section_fields = []
            if isinstance(section_data, dict) and 'properties' in section_data:
                for field, field_details in section_data['properties'].items():
                    if isinstance(field_details, dict):
                        field_details['field_name'] = field
                    django_field, imports = get_django_field_type(field_details, field_details, class_name, is_world=False)
                    required_imports.update(imports)
                    section_fields.append((field, django_field))
            if section_fields:
                fields.append((section, section_fields))
                
    return fields, required_imports

def generate_django_model(class_name, fields, required_imports, is_world=False):
    """Generate Django model class string from field definitions."""
    # Determine base class
    base_class = 'AbstractBaseModel' if is_world else 'AbstractElementModel'
    model = f"class {class_name}({base_class}):\n"
    
    if is_world:
        required_imports.add("models") # Manager needs models
        model += "    objects = models.Manager()\n"
        for field, field_type in fields:
            model += f"    {field} = {field_type}\n"
    elif class_name == 'Pin':
        # Special case for Pin model GFK
        required_imports.add("models")
        required_imports.add("contenttypes")
        required_imports.add("uuid") # For object_id
        
        for section_name, section_fields in fields:
            model += f"\n    # {section_name.capitalize()}\n"
            for field, field_type in section_fields:
                # Skip the original 'element' field derived from YAML
                if field == 'element': 
                    continue
                model += f"    {field} = {field_type}\n"
        
        # Add the GenericForeignKey fields 
        model += "    content_type = models.ForeignKey(ContentType, on_delete=models.SET_NULL, blank=True, null=True)\n"
        model += "    object_id = models.UUIDField(blank=True, null=True)\n"
        model += "    element = GenericForeignKey('content_type', 'object_id')\n"

    else: # Standard element model generation
        for section_name, section_fields in fields:
            model += f"\n    # {section_name.capitalize()}\n"
            for field, field_type in section_fields:
                model += f"    {field} = {field_type}\n"
    
    model += "\n    def __str__(self):\n        return self.name\n"
    return model, required_imports

def generate_import_statements(required_imports, class_name, is_world, is_abstract=False):
    """Generate import statements based on collected requirements."""
    import_lines = []
    if "models" in required_imports:
        import_lines.append("from django.db import models")
    if "uuid" in required_imports:
        import_lines.append("import uuid")
    if "validators" in required_imports:
        import_lines.append("from django.core.validators import MaxValueValidator")
    if "contenttypes" in required_imports:
        import_lines.append("from django.contrib.contenttypes.fields import GenericForeignKey")
        import_lines.append("from django.contrib.contenttypes.models import ContentType")

    # Add base model import unless it's the abstract model itself
    if not is_abstract:
        if is_world:
            # Assuming a base model exists for World, adjust if needed
            # import_lines.append("from .abstract_base_model import AbstractBaseModel") 
            pass # No abstract base for World currently defined
        else:
            import_lines.append(f"from .abstract_element_model import AbstractElementModel")
            
    return "\n".join(import_lines) + "\n\n" if import_lines else ""


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
    django_dir = os.path.join(script_directory, '..', 'conversions', 'django_models')
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
