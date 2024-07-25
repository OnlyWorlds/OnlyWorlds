import os
import yaml

def generate_obsidian_template(yaml_content, template_path):
    with open(template_path, 'w') as md_file:
        if 'properties' in yaml_content:
            for section, section_content in yaml_content['properties'].items():
                md_file.write(f"## {section.capitalize()}\n")
                for field, details in section_content.get('properties', {}).items():
                    field_name = field.capitalize()
                    field_type = details.get('type', 'text')  # Default to text if type is not specified

                    # Adjust tooltip text based on the type
                    if field_type == 'integer':
                        field_type = "number-field"
                        tooltip = "Number"
                    elif 'items' in details or field_type == 'multi-link':
                        field_type = "multi-link-field"
                        tooltip = f"Multi {details.get('category', '').strip()}"
                    elif field_type == 'single-link':
                        field_type = "link-field"
                        tooltip = f"Single {details.get('category', '').strip()}"
                    else:
                        field_type = "text-field"  # Ensure string types are represented as text-field
                        tooltip = "Text"

                    # Write the field to the markdown file
                    md_file.write(f"- <span class=\"{field_type}\" data-tooltip=\"{tooltip}\">{field_name}</span>: \n")
                md_file.write("\n")
        else:
            print(f"No 'properties' key found in YAML file for {template_path}")

def convert_yaml_to_md(yaml_path, md_path):
    with open(yaml_path, 'r') as yaml_file:
        yaml_content = yaml.safe_load(yaml_file)
    generate_obsidian_template(yaml_content, md_path)

if __name__ == "__main__":
    script_directory = os.path.dirname(__file__)
    yaml_dir = os.path.join(script_directory, '..', 'schema')
    md_dir = os.path.join(script_directory, '..', 'languages', 'obsidian_templates')

    os.makedirs(md_dir, exist_ok=True)

    for filename in os.listdir(yaml_dir):
        if filename.endswith('.yaml'):
            yaml_path = os.path.join(yaml_dir, filename)
            md_filename = filename.replace('.yaml', '.md')
            md_path = os.path.join(md_dir, md_filename)
            convert_yaml_to_md(yaml_path, md_path)
            print(f"Converted {filename} to Markdown Template: {md_filename}")
