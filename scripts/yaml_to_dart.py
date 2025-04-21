import os
import yaml

def get_dart_type(yaml_type, field_details=None):
    """Determine Dart type from YAML type information."""
    # If field_details is provided and has type info, use it preferentially
    current_type_info = field_details if isinstance(field_details, dict) and 'type' in field_details else yaml_type

    if isinstance(current_type_info, dict):
        field_type = current_type_info.get('type')
        if field_type == 'integer':
            return 'int'
        elif field_type == 'string' or current_type_info.get('format') in ['uuid', 'url'] :
             return 'String'
        elif field_type == 'array':
            items = current_type_info.get('items', {})
            item_type = items.get('type')
            if item_type == 'integer':
                return 'List<int>'
            elif item_type == 'string':
                return 'List<String>'
            else:
                return 'List<dynamic>' # Fallback for unknown item types
        elif field_type in ['multi-link', 'single-link']:
             return 'String' # Represent links as String IDs

    # Handle cases where yaml_type is just a string (less common with full schema)
    elif isinstance(yaml_type, str):
        if yaml_type == 'Integer':
            return 'int'
        elif yaml_type in ['String', 'UUID', 'URL'] or '|' in yaml_type:
            return 'String'

    # Default to String for unknown or unspecified types
    return 'String'

def snake_to_camel(snake_str):
    """Convert snake_case to camelCase."""
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

def generate_comment(field_details):
    """Generate field comment based on field details."""
    if not isinstance(field_details, dict):
        return ''
    
    comment = ''
    field_type = field_details.get('type', '')
    
    # Add link type comments
    if field_type in ['multi-link', 'single-link'] and 'category' in field_details:
        category = field_details.get('category', '')
        prefix = 'ms' if field_type == 'multi-link' else 'ss'
        comment = f' //{prefix} {category.lower()}'
    # Add max value comments for integers
    elif field_type == 'integer' and 'maximum' in field_details and field_details['maximum'] > 0:
        comment = f' // maxint'
    
    return comment

def extract_fields(yaml_data, is_world=False):
    """Extract field definitions from YAML data."""
    fields = []

    if 'properties' not in yaml_data:
        return fields # No properties to extract

    # Handle World schema specifically (flat structure under 'properties')
    if is_world:
        for field, field_details in yaml_data['properties'].items():
            dart_type = get_dart_type(field_details, field_details) # Pass details for better type inference
            field_name = snake_to_camel(field)
            comment = generate_comment(field_details)
            fields.append((field_name, dart_type, comment))
    # Handle other schemas with potentially nested properties sections
    else:
        for section, section_data in yaml_data['properties'].items():
            section_fields = []

            if isinstance(section_data, dict) and 'properties' in section_data:
                for field, field_details in section_data['properties'].items():
                    dart_type = get_dart_type(field_details, field_details) # Pass details
                    field_name = snake_to_camel(field)
                    comment = generate_comment(field_details)
                    section_fields.append((field_name, dart_type, comment))

            if section_fields:
                fields.append((section, section_fields))

    return fields

def generate_dart_class(class_name, fields, base_class=None):
    """Generate Dart class from field definitions."""
    dart_class = f'class {class_name} ' + (f'extends {base_class} ' if base_class else '') + '{\n'
    
    # Handle World class (flat list of fields)
    if not any(isinstance(item, tuple) and isinstance(item[1], list) for item in fields):
        for field_name, dart_type, comment in fields:
            dart_class += f'  final {dart_type} {field_name};{comment}\n'
    # Handle other classes (grouped by sections)
    else:
        for section, section_fields in fields:
            dart_class += f'  // {section.capitalize()}\n'
            for field_name, dart_type, comment in section_fields:
                dart_class += f'  final {dart_type} {field_name};{comment}\n'
    
    dart_class += '}\n'
    return dart_class

def write_dart_file(directory, filename, content):
    """Write content to a file."""
    with open(os.path.join(directory, filename), 'w') as file:
        file.write(content)

def load_base_properties(base_path):
    """Load base properties from YAML file."""
    with open(base_path, 'r') as file:
        base_data = yaml.safe_load(file)
        return base_data['properties']

def extract_base_fields(base_properties):
    """Extract base fields for the BaseModel class."""
    fields = []
    for field, details in base_properties.items():
        dart_type = get_dart_type(details)
        # Special case for Image_URL to match existing code
        if field == 'Image_URL':
            field = 'imageURL'
        fields.append((field.lower(), dart_type))
    return fields

def create_base_model(base_properties):
    """Create the BaseModel abstract class content."""
    dart_class = 'abstract class BaseElement {\n'
    
    for field, dart_type in extract_base_fields(base_properties):
        dart_class += f'  {dart_type} {field};\n'
    
    dart_class += '}\n'
    return dart_class

if __name__ == "__main__":
    # Define paths
    script_directory = os.path.dirname(__file__)
    yaml_dir = os.path.join(script_directory, '..', 'schema')
    dart_dir = os.path.join(script_directory, '..', 'conversions', 'dart')
    base_path = os.path.join(yaml_dir, 'base_properties.yaml')
    
    # Create output directory
    os.makedirs(dart_dir, exist_ok=True)
    
    # Load base properties
    base_properties = load_base_properties(base_path)
    
    # Generate and write the BaseModel abstract class
    base_model_content = create_base_model(base_properties)
    write_dart_file(dart_dir, 'base_element.dart', base_model_content)
    print('Generated base_element.dart')
    
    # Process each YAML file
    for filename in os.listdir(yaml_dir):
        if filename.endswith('.yaml') and filename != 'base_properties.yaml':
            yaml_path = os.path.join(yaml_dir, filename)
            with open(yaml_path, 'r') as yaml_file:
                yaml_content = yaml.safe_load(yaml_file)
                
                # Determine class name from filename
                class_name = filename.replace('.yaml', '').capitalize()
                is_world = class_name == 'World'
                
                # Extract fields
                fields = extract_fields(yaml_content, is_world)
                
                # Generate class
                dart_class = generate_dart_class(
                    class_name, 
                    fields, 
                    'BaseElement' if not is_world else None
                )
                
                # Write to file
                dart_filename = f'{class_name.lower()}.dart'
                write_dart_file(dart_dir, dart_filename, dart_class)
                print(f'Generated {dart_filename}') 