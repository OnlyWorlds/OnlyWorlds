import os
import yaml

# Function to convert YAML to Dart class

def yaml_to_dart_class(yaml_content, class_name, base_class=None):
    dart_class = f'class {class_name} ' + (f'extends {base_class} ' if base_class else '') + '{\n'
    
    # Process fields based on class type
    if class_name == 'World':
        # Process World fields
        for field, field_type in yaml_content.items():
            if isinstance(field_type, dict) and 'type' in field_type and field_type['type'] == 'List':
                dart_type = 'String'  # Lists are stored as strings in Dart
            elif field_type == 'Integer' or field_type == 'int':
                dart_type = 'int'
            else:
                dart_type = 'String'
            
            # Convert field name from snake_case to camelCase
            field_name = ''.join(word.capitalize() if i > 0 else word for i, word in enumerate(field.split('_')))
            
            dart_class += f'  final {dart_type} {field_name};\n'
    else:
        # Process other classes with nested properties
        if 'properties' in yaml_content:
            # Process each section (constitution, origins, etc.)
            for section, section_content in yaml_content['properties'].items():
                dart_class += f'  // {section.capitalize()}\n'
                
                if isinstance(section_content, dict) and 'properties' in section_content:
                    # Process each property in this section
                    for field, field_details in section_content['properties'].items():
                        if isinstance(field_details, dict):
                            field_type = field_details.get('type', '')
                            
                            # Determine Dart type based on field type
                            if field_type == 'integer':
                                dart_type = 'int'
                            else:
                                dart_type = 'String'
                            
                            # Convert field name from snake_case to camelCase if needed
                            field_name = ''.join(word.capitalize() if i > 0 else word for i, word in enumerate(field.split('_')))
                            
                            # Add special comments for references to other types
                            comment = ''
                            if field_type in ['multi-link', 'single-link'] and 'category' in field_details:
                                category = field_details.get('category', '')
                                prefix = 'ms' if field_type == 'multi-link' else 'ss'
                                comment = f' //{prefix} {category.lower()}'
                            elif field_type == 'integer' and 'maximum' in field_details and field_details['maximum'] > 0:
                                comment = f' // maxint'
                            
                            dart_class += f'  final {dart_type} {field_name};{comment}\n'
    
    dart_class += '}\n'
    return dart_class

# Function to write Dart class to file

def write_dart_file(directory, filename, content):
    with open(os.path.join(directory, filename), 'w') as file:
        file.write(content)

if __name__ == "__main__":
    # Define paths
    script_directory = os.path.dirname(__file__)
    yaml_dir = os.path.join(script_directory, '..', 'schema')
    dart_dir = os.path.join(script_directory, '..', 'languages', 'dart')
    os.makedirs(dart_dir, exist_ok=True)

    # Base model
    base_model_content = '''
abstract class BaseModel {
  String id;
  String name;
  String description;
  String supertype;
  String subtype;
  String imageURL;
}
'''
    write_dart_file(dart_dir, 'base_model.dart', base_model_content)

    # Convert each YAML file to a Dart class
    for filename in os.listdir(yaml_dir):
        if filename.endswith('.yaml') and filename != 'base_properties.yaml':
            yaml_path = os.path.join(yaml_dir, filename)
            with open(yaml_path, 'r') as yaml_file:
                yaml_content = yaml.safe_load(yaml_file)
                class_name = filename.replace('.yaml', '').capitalize()
                if class_name == 'World':
                    dart_class = yaml_to_dart_class(yaml_content['World'], class_name)
                else:
                    dart_class = yaml_to_dart_class(yaml_content, class_name, 'BaseModel')
                write_dart_file(dart_dir, f'{class_name.lower()}.dart', dart_class)
                print(f'Converted {filename} to Dart class: {class_name}') 