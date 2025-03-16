import os
import yaml

def get_django_field_type(yaml_type, field_details=None, model_name=None, is_world=False):
    """Determine Django field type based on YAML type."""
    if isinstance(yaml_type, dict):
        yaml_type_str = yaml_type.get('type', '')
        if yaml_type_str == 'integer':
            if isinstance(field_details, dict) and 'maximum' in field_details and field_details['maximum'] > 0:
                return f"models.PositiveIntegerField(blank=True, null=True, validators=[MaxValueValidator({field_details['maximum']})])" if not is_world else f"models.PositiveIntegerField(validators=[MaxValueValidator({field_details['maximum']})])"
            return "models.PositiveIntegerField(blank=True, null=True)" if not is_world else "models.PositiveIntegerField()"
        elif yaml_type_str == 'string':
            return "models.TextField(blank=True, null=True)" if not is_world else "models.TextField()"
        elif yaml_type_str == 'multi-link':
            if isinstance(field_details, dict) and 'category' in field_details:
                category = field_details['category']
                field_name = field_details.get('field_name', '')
                related_name = f'"{model_name.lower()}_{field_name}"' if model_name and field_name else None
                return f'models.ManyToManyField("{category}", blank=True, related_name={related_name})' if related_name else f'models.ManyToManyField("{category}", blank=True)'
            return 'models.ManyToManyField("Element", blank=True)'
        elif yaml_type_str == 'single-link':
            if isinstance(field_details, dict) and 'category' in field_details:
                category = field_details['category']
                field_name = field_details.get('field_name', '')
                related_name = f'"{model_name.lower()}_{field_name}"' if model_name and field_name else None
                return f'models.ForeignKey("{category}", on_delete=models.SET_NULL, blank=True, null=True, related_name={related_name})' if related_name else f'models.ForeignKey("{category}", on_delete=models.SET_NULL, blank=True, null=True)'
            return 'models.ForeignKey("Element", on_delete=models.SET_NULL, blank=True, null=True)'
        elif yaml_type_str == 'List':
            return "JSONField(default=list)"
    elif isinstance(yaml_type, str):
        if yaml_type == 'UUID':
            return "models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)"
        elif yaml_type == 'String':
            if isinstance(field_details, dict) and field_details.get('field_name') == 'api_key':
                return "models.CharField(max_length=10, unique=True)"
            return "models.CharField(max_length=255, blank=True, null=True)" if not is_world else "models.CharField(max_length=255)"
        elif yaml_type == 'Integer':
            return "models.PositiveIntegerField(blank=True, null=True)" if not is_world else "models.PositiveIntegerField()"
        elif yaml_type == 'URL':
            return "models.URLField(blank=True, null=True)"
    return "models.TextField(blank=True, null=True)" if not is_world else "models.TextField()"

def extract_fields(yaml_data, class_name=None, is_world=False):
    """Extract field definitions from YAML data."""
    fields = []
    
    if is_world and 'World' in yaml_data:
        for field, field_type in yaml_data['World'].items():
            if isinstance(field_type, dict):
                field_type['field_name'] = field
            django_field = get_django_field_type(field_type, field_type, 'World', is_world=True)
            fields.append((field, django_field))
    elif 'properties' in yaml_data:
        for section, section_data in yaml_data['properties'].items():
            section_fields = []
            if isinstance(section_data, dict) and 'properties' in section_data:
                for field, field_details in section_data['properties'].items():
                    if isinstance(field_details, dict):
                        field_details['field_name'] = field
                    django_field = get_django_field_type(field_details, field_details, class_name, is_world=False)
                    section_fields.append((field, django_field))
            if section_fields:
                fields.append((section, section_fields))
    return fields

def generate_django_model(class_name, fields, is_world=False):
    """Generate Django model class from field definitions."""
    model = f"class {class_name}({'AbstractBaseModel' if is_world else 'AbstractElementModel'}):\n"
    
    if is_world:
        model += "    objects = models.Manager()\n"
        for field, field_type in fields:
            model += f"    {field} = {field_type}\n"
    else:
        for section_name, section_fields in fields:
            model += f"\n    # {section_name.capitalize()}\n"
            for field, field_type in section_fields:
                model += f"    {field} = {field_type}\n"
    
    model += "\n    def __str__(self):\n        return self.name\n"
    return model

def write_django_file(directory, filename, content):
    """Write content to a file."""
    with open(os.path.join(directory, filename), 'w') as file:
        file.write(content)

def convert_yaml_to_django(yaml_path, django_path):
    """Convert YAML file to Django model."""
    with open(yaml_path, 'r') as yaml_file:
        yaml_content = yaml.safe_load(yaml_file)
    
    filename = os.path.basename(yaml_path)
    class_name = filename.replace('.yaml', '').capitalize()
    is_world = class_name == 'World'
    
    fields = extract_fields(yaml_content, class_name, is_world)
    django_model = generate_django_model(class_name, fields, is_world)
    
    write_django_file(django_path, f"{filename.replace('.yaml', '')}.py", django_model)
    print(f"Generated Django model for {class_name}")

if __name__ == "__main__":
    script_directory = os.path.dirname(__file__)
    yaml_dir = os.path.join(script_directory, '..', 'schema')
    django_dir = os.path.join(script_directory, '..', 'languages', 'django')
    
    os.makedirs(django_dir, exist_ok=True)
    
    for filename in os.listdir(yaml_dir):
        if filename.endswith('.yaml') and filename != 'base_properties.yaml':
            yaml_path = os.path.join(yaml_dir, filename)
            convert_yaml_to_django(yaml_path, django_dir)
