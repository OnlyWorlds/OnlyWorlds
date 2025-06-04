import os
import json
import yaml

def load_yaml_data(yaml_path):
    """Load full data from a YAML file."""
    try:
        with open(yaml_path, 'r', encoding='utf-8') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        print(f"Error: YAML file not found at {yaml_path}")
        return None
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file {yaml_path}: {e}")
        return None

def generate_json(data, json_path):
    """Generate a JSON file from the provided data."""
    if data is None:
        print(f"Skipping JSON generation for {os.path.basename(json_path)} due to load error.")
        return
    try:
        with open(json_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Generated {os.path.basename(json_path)}")
    except IOError as e:
        print(f"Error writing JSON file {json_path}: {e}")

if __name__ == "__main__":
    # Define paths relative to the script location.
    script_directory = os.path.dirname(__file__)
    yaml_dir = os.path.join(script_directory, '..', 'schema')
    json_dir = os.path.join(script_directory, '..', 'languages', 'json')

    # Create the output directory if it doesn't exist.
    os.makedirs(json_dir, exist_ok=True)

    # Process all YAML files in the schema folder.
    for filename in os.listdir(yaml_dir):
        if filename.endswith('.yaml'):
            yaml_path = os.path.join(yaml_dir, filename)
            json_path = os.path.join(json_dir, filename.replace('.yaml', '.json'))
            
            # Load the full YAML data
            yaml_data = load_yaml_data(yaml_path)
            
            # Generate the corresponding JSON file, preserving the structure
            generate_json(yaml_data, json_path)
