import os
import json
import yaml
from collections import OrderedDict

def load_base_properties(base_path):
    """Load base properties from the YAML file."""
    with open(base_path, 'r') as file:
        base_data = yaml.safe_load(file)
        return base_data['properties']  # Extract only the properties part.

def generate_base_properties_json(base_properties, json_path):
    """Generate a separate base_properties.json file."""
    with open(json_path, 'w') as json_file:
        json.dump({"properties": base_properties}, json_file, indent=4)
    print(f"Generated base_properties.json")

def convert_yaml_to_json(yaml_path, json_path):
    """Convert YAML file to JSON file without including base properties."""
    with open(yaml_path, 'r') as yaml_file:
        category_properties = yaml.safe_load(yaml_file)
    
    with open(json_path, 'w') as json_file:
        json.dump(category_properties, json_file, indent=4)

if __name__ == "__main__":
    # Define paths relative to the script location.
    script_directory = os.path.dirname(__file__)
    yaml_dir = os.path.join(script_directory, '..', 'schema')
    json_dir = os.path.join(script_directory, '..', 'languages', 'json')
    base_path = os.path.join(yaml_dir, 'base_properties.yaml')

    # Load base properties from the designated YAML file.
    base_properties = load_base_properties(base_path)

    # Create the output directory if it doesn't exist.
    os.makedirs(json_dir, exist_ok=True)
    
    # Generate the base_properties.json file
    base_json_path = os.path.join(json_dir, 'base_properties.json')
    generate_base_properties_json(base_properties, base_json_path)

    # Convert all YAML files in the schema folder to JSON without base properties.
    for filename in os.listdir(yaml_dir):
        if filename.endswith('.yaml') and filename != 'base_properties.yaml':
            yaml_path = os.path.join(yaml_dir, filename)
            json_path = os.path.join(json_dir, filename.replace('.yaml', '.json'))
            convert_yaml_to_json(yaml_path, json_path)
            print(f"Converted {filename} to JSON")
