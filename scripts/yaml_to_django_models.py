import os
import yaml
from collections import defaultdict
 

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
    base_attrs = "" if is_required else ", blank=True, null=True"
    # SET_NULL requires null=True, PROTECT is better if null is False
    fk_on_delete = "models.PROTECT" if is_required else "models.CASCADE" # Cascade for World FK seems reasonable
    fk_attrs = f", on_delete={fk_on_delete}" + ("" if is_required else ", blank=True, null=True") # Though World FK is required by structure

    # Handle special fields for the base model - ID and Name are inherently required
    if field_name.lower() == 'id':
        required_imports.add("uuid")
        return "models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)", description, required_imports
    elif field_name.lower() == 'name':
        return "models.TextField(max_length=255)", description, required_imports # Always required
    elif field_name.lower() == 'description':
         # Description can be optional unless explicitly required
        return f"models.TextField({base_attrs.lstrip(', ')})", description, required_imports
    elif field_name.lower() == 'image_url':
         # Image URL can be optional unless explicitly required
        return f"models.URLField({base_attrs.lstrip(', ')})", description, required_imports
    elif field_name.lower() == 'world':
        # World FK is always required for an element, hence no blank/null
        return ('models.ForeignKey(\n        "worlds.World",\n        on_delete=models.CASCADE,'
                '\n        related_name="%(class)s_related",\n    )', description, required_imports)
    
    # General field type mapping (less likely needed with current base_properties)
    if field_type == 'integer':
        if maximum:
            required_imports.add("validators")
            validators_str = f", validators=[MaxValueValidator({maximum})]"
            # Assuming base integer fields are nullable unless required
            return f"models.PositiveIntegerField(validators=[MaxValueValidator({maximum})]{base_attrs})", description, required_imports
        return f"models.IntegerField({base_attrs.lstrip(', ')})", description, required_imports
    elif field_type == 'string':
        # Assuming base string fields are nullable unless required
        return f"models.CharField(max_length=255{base_attrs})", description, required_imports
    else:
         # Default to nullable TextField unless required
        return f"models.TextField({base_attrs.lstrip(', ')})", description, required_imports

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


def extract_fields(yaml_data, class_name=None, is_world=False):
    """Extract field definitions from YAML data and collect required imports."""
    fields = []
    required_imports = set()
    
    # Handle World fields separately if needed (currently no required logic shown here)
    if is_world and 'World' in yaml_data:
        # Assuming 'World' structure doesn't use 'required' keyword like element properties
        world_props = yaml_data['World']
        for field, field_type in world_props.items():
            if isinstance(field_type, dict):
                field_type['field_name'] = field
            # World fields are treated as required by default in get_django_field_type
            django_field, imports = get_django_field_type(field_type, field_type, 'World', is_world=True, is_required=True) 
            required_imports.update(imports)
            fields.append((field, django_field))
    elif 'properties' in yaml_data:
        top_level_properties = yaml_data['properties']
        # Check for required fields at the top level (less common for nested structure)
        top_level_required = yaml_data.get('required', []) 

        for section, section_data in top_level_properties.items():
            section_fields = []
            # Check if this section represents a nested object with its own properties and requirements
            if isinstance(section_data, dict) and section_data.get('type') == 'object' and 'properties' in section_data:
                nested_properties = section_data['properties']
                # Get the list of required fields *within* this nested object
                nested_required = section_data.get('required', []) 
                
                for field, field_details in nested_properties.items():
                    if isinstance(field_details, dict):
                        field_details['field_name'] = field # Add field name for context if needed
                    
                    # Determine if the current field is required within its nested section
                    is_field_required = field in nested_required
                    
                    # Pass the is_field_required status to the type getter
                    django_field, imports = get_django_field_type(
                        field_details, field_details, class_name, is_world=False, is_required=is_field_required
                    )
                    required_imports.update(imports)
                    section_fields.append((field, django_field))
            # Handle simpler top-level fields if necessary (might need adjustment based on schema design)
            # elif section not in ['title', '$schema', 'type', 'description', 'version']: # Example check
            #     is_field_required = section in top_level_required
            #     django_field, imports = get_django_field_type(section_data, section_data, class_name, is_world=False, is_required=is_field_required)
            #     required_imports.update(imports)
            #     # Decide how to structure fields if not nested under 'details', 'meta' etc.
            #     # This part might need refinement based on actual YAML structures used.
            #     # For now, assuming primary fields are under nested objects like 'details'.
            #     pass 

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
