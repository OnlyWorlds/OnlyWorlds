import os
import json
import yaml

def convert_yaml_to_json(yaml_path, json_path):
    with open(yaml_path, 'r') as yaml_file:
        yaml_content = yaml.safe_load(yaml_file)
    with open(json_path, 'w') as json_file:
        json.dump(yaml_content, json_file, indent=4)

if __name__ == "__main__":
    # Define paths relative to the script location.
    script_directory = os.path.dirname(__file__)  # Get the directory where the script is located.
    yaml_dir = os.path.join(script_directory, '..', 'schema')  # Path to the schema directory.
    json_dir = os.path.join(script_directory, '..', 'languages', 'json')   # Path to the languages directory for JSON output.

    # Create the output directory if it doesn't exist.
    os.makedirs(json_dir, exist_ok=True)

    # Convert all YAML files in the schema folder to JSON in the languages folder.
    for filename in os.listdir(yaml_dir):
        if filename.endswith('.yaml'):
            yaml_path = os.path.join(yaml_dir, filename)
            json_path = os.path.join(json_dir, filename.replace('.yaml', '.json'))
            convert_yaml_to_json(yaml_path, json_path)
            print(f"Converted {filename} to JSON")
