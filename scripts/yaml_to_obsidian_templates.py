import os
import yaml

def generate_obsidian_template(base_properties, yaml_content, template_path):
    with open(template_path, 'w') as md_file:
        # Write the 'Base' properties first
        md_file.write("## Base\n")
        for field, details in base_properties.items():
            tooltip = "Text" if details.get('type', 'string') == 'string' else "Number"
            md_file.write(f"- <span class=\"text-field\" data-tooltip=\"{tooltip}\">{field}</span>: \n")
        md_file.write("\n")

        # Then write other properties from the category
        if 'properties' in yaml_content:
            for section, section_content in yaml_content['properties'].items():
                md_file.write(f"## {section.capitalize()}\n")
                for field, details in section_content.get('properties', {}).items():
                    field_name = field.capitalize()
                    field_type = details.get('type', 'text')  # Default to text if type is not specified

                    max_value = details.get('maximum')
                    if field_type == 'integer' and max_value is not None:
                        field_type = "number-field"
                        tooltip = f"Number, max: {max_value}"
                    elif field_type == 'integer':
                        field_type = "number-field"
                        tooltip = "Number"
                    elif 'items' in details or field_type == 'multi-link':
                        field_type = "multi-link-field"
                        tooltip = f"Multi {details.get('category', '').strip()}"
                    elif field_type == 'single-link':
                        field_type = "link-field"
                        tooltip = f"Single {details.get('category', '').strip()}"
                    else:
                        field_type = "text-field"
                        tooltip = "Text"

                    # Write the field to the markdown file
                    md_file.write(f"- <span class=\"{field_type}\" data-tooltip=\"{tooltip}\">{field_name}</span>: \n")
                md_file.write("\n")

def convert_yaml_to_md(base_properties, yaml_path, md_path):
    with open(yaml_path, 'r') as yaml_file:
        yaml_content = yaml.safe_load(yaml_file)
    generate_obsidian_template(base_properties, yaml_content, md_path)

if __name__ == "__main__":
    script_directory = os.path.dirname(__file__)
    yaml_dir = os.path.join(script_directory, '..', 'schema')
    md_dir = os.path.join(script_directory, '..', 'languages', 'obsidian_templates')
    base_path = os.path.join(yaml_dir, 'base_properties.yaml')

    # Load base properties once
    with open(base_path, 'r') as file:
        base_properties = yaml.safe_load(file)['properties']

    os.makedirs(md_dir, exist_ok=True)

    files_to_exclude = ['base_properties.yaml', 'world.yaml', 'map.yaml', 'pin.yaml', 'marker.yaml']
    for filename in os.listdir(yaml_dir):
        if filename.endswith('.yaml') and filename not in files_to_exclude:
            yaml_path = os.path.join(yaml_dir, filename)
            md_filename = filename[:-5].capitalize() + '.md'
            md_path = os.path.join(md_dir, md_filename)
            convert_yaml_to_md(base_properties, yaml_path, md_path)
            print(f"Converted {filename} to Markdown Template: {md_filename}")
