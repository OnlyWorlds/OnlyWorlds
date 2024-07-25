import os
import yaml

def generate_handlebars_template(yaml_content, template_path):
    with open(template_path, 'w') as md_file:
        if 'properties' in yaml_content:
            for section, section_content in yaml_content['properties'].items():
                md_file.write(f"## {section.capitalize()}\n")
                for field, details in section_content.get('properties', {}).items():
                    field_name = field.capitalize()
                    field_variable = field.lower()
                    field_type = details.get('type', 'text')

                    # Determine tooltip and append handlebars syntax
                    if field_type == 'integer':
                        field_type = "number-field"
                        tooltip = "Number"
                        handlebars_value = f"{{{{{field_variable}}}}}"
                    elif 'items' in details or field_type == 'multi-link':
                        field_type = "multi-link-field"
                        tooltip = f"Multi {details.get('category', '').strip()}"
                        handlebars_value = f"{{{{linkify {field_variable}}}}}"
                    elif field_type == 'single-link':
                        field_type = "link-field"
                        tooltip = f"Single {details.get('category', '').strip()}"
                        handlebars_value = f"{{{{linkify {field_variable}}}}}"
                    else:
                        field_type = "text-field"
                        tooltip = "Text"
                        handlebars_value = f"{{{{{field_variable}}}}}"

                    # Write the field to the markdown file
                    md_file.write(f"- <span class=\"{field_type}\" data-tooltip=\"{tooltip}\">{field_name}</span>: {handlebars_value}\n")
                md_file.write("\n")
        else:
            print(f"No 'properties' key found in YAML file for {template_path}")

def convert_yaml_to_handlebars(yaml_path, handlebars_path):
    with open(yaml_path, 'r') as yaml_file:
        yaml_content = yaml.safe_load(yaml_file)
    generate_handlebars_template(yaml_content, handlebars_path)

if __name__ == "__main__":
    script_directory = os.path.dirname(__file__)
    yaml_dir = os.path.join(script_directory, '..', 'schema')
    handlebars_dir = os.path.join(script_directory, '..', 'languages', 'obsidian_handlebars')

    os.makedirs(handlebars_dir, exist_ok=True)

    for filename in os.listdir(yaml_dir):
        if filename.endswith('.yaml'):
            yaml_path = os.path.join(yaml_dir, filename)
            handlebars_filename = filename.replace('.yaml', '.md')
            handlebars_path = os.path.join(handlebars_dir, handlebars_filename)
            convert_yaml_to_handlebars(yaml_path, handlebars_path)
            print(f"Converted {filename} to Handlebars Template: {handlebars_filename}")
