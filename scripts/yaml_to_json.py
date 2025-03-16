import os
import json
import yaml
from collections import OrderedDict

def load_base_properties(base_path):
    """Load base properties from the YAML file."""
    with open(base_path, 'r') as file:
        base_data = yaml.safe_load(file)
        return base_data['properties']  # Extract only the properties part.

def merge_properties(base_properties, category_properties, is_world=False):
    """Merge base properties under 'Base' header into category-specific properties."""
    # Create an ordered dictionary to preserve the order of insertion.
    ordered_properties = OrderedDict()
    
    if not is_world:
        ordered_properties['Base'] = base_properties  # Insert the base properties first.
    
    # Check if there are existing properties and add them after the base properties.
    if 'properties' in category_properties:
        for key, value in category_properties['properties'].items():
            ordered_properties[key] = value

    # Replace the original properties with our new ordered dictionary.
    category_properties['properties'] = ordered_properties
    return category_properties

def convert_yaml_to_json(base_properties, yaml_path, json_path):
    """Convert YAML file to JSON file with base properties included under 'Base' header and placed at the top."""
    with open(yaml_path, 'r') as yaml_file:
        category_properties = yaml.safe_load(yaml_file)
        
        # Check if this is the world.yaml file
        filename = os.path.basename(yaml_path)
        is_world = filename == 'world.yaml'
        
        merged_properties = merge_properties(base_properties, category_properties, is_world)
    with open(json_path, 'w') as json_file:
        json.dump(merged_properties, json_file, indent=4)

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

    # Convert all YAML files in the schema folder to JSON, including base properties under 'Base'.
    for filename in os.listdir(yaml_dir):
        if filename.endswith('.yaml') and filename != 'base_properties.yaml':
            yaml_path = os.path.join(yaml_dir, filename)
            json_path = os.path.join(json_dir, filename.replace('.yaml', '.json'))
            convert_yaml_to_json(base_properties, yaml_path, json_path)
            print(f"Converted {filename} to JSON")
