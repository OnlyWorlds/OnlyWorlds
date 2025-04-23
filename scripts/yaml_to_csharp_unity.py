import os
import yaml
import re
import logging
from pathlib import Path
from typing import Tuple, Dict, Any, Set, List

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# --- Constants ---
BASE_PROPERTIES_FILENAME = "base_properties.yaml"

# --- Helper Functions ---

def to_pascal_case(snake_str):
    """Converts snake_case, camelCase, PascalCase, or kebab-case to PascalCase."""
    if not snake_str:
        return ""
    # Split by underscore, hyphen, or detect case change for camelCase/PascalCase
    components = re.split('_|-|(?=[A-Z])', snake_str)
    # Capitalize the first letter of each component and join
    return ''.join(x.capitalize() for x in components if x)

def map_yaml_type_to_csharp(yaml_prop: Dict[str, Any], field_name_original: str, is_required: bool) -> Tuple[str, str, bool]:
    """Maps YAML type properties to C# type string, transformed PascalCase field name, and whether it's a list."""
    yaml_type = yaml_prop.get("type")
    category = yaml_prop.get("category")
    cs_type = "object" # Default fallback
    original_pascal_case_name = to_pascal_case(field_name_original)
    cs_field_name = original_pascal_case_name # Start with PascalCase
    is_list = False
    needs_nullable_marker = not is_required # Value types need '?' if not required

    if yaml_type == "string":
        cs_type = "string"
        needs_nullable_marker = False # string is reference type, already nullable
    elif yaml_type == "integer":
        cs_type = "int"
    elif yaml_type == "boolean":
        cs_type = "bool"
    elif yaml_type == "array":
        is_list = True
        needs_nullable_marker = False # List<> is reference type
        items_prop = yaml_prop.get("items", {})
        item_yaml_type = items_prop.get("type", "string") # Default to string if item type not specified
        item_type = "object"
        if item_yaml_type == "string":
            item_type = "string"
        elif item_yaml_type == "integer":
            item_type = "int"
        elif item_yaml_type == "boolean":
             item_type = "bool"
        else:
             logging.warning(f"Unhandled array item type '{item_yaml_type}' for field '{field_name_original}'. Defaulting to List<object>.")
        cs_type = f"List<{item_type}>"
    elif yaml_type == "single-link":
        cs_type = "string" # Represent link by ID
        needs_nullable_marker = False
        if field_name_original.lower() == "world":
             cs_field_name = "WorldId"
        else:
             cs_field_name = original_pascal_case_name + "Id"
        if not category and field_name_original.lower() != "world":
            logging.warning(f"Field '{field_name_original}' is single-link but has no category.")
    elif yaml_type == "multi-link":
        cs_type = "List<string>" # Array of IDs
        needs_nullable_marker = False
        is_list = True
        cs_field_name = original_pascal_case_name + "Ids"
        if not category:
            logging.warning(f"Field '{field_name_original}' is multi-link but has no category.")
    elif yaml_type == "generic-link":
         cs_type = "string"
         needs_nullable_marker = False
         cs_field_name = original_pascal_case_name + "Id"
    else:
        if yaml_type not in ["object"]:
             logging.warning(f"Unknown YAML type '{yaml_type}' for field '{field_name_original}'. Defaulting to 'object'.")

    # Add nullable marker for value types if needed
    if needs_nullable_marker and cs_type in ["int", "bool"]: # Add other value types if needed
         cs_type += "?"

    return cs_type, cs_field_name, is_list

def parse_base_properties(schema_dir: Path) -> Tuple[Dict[str, Any], Set[str]]:
    """Parses the base_properties.yaml file.

    Returns:
        A tuple containing: (properties dictionary, set of required ORIGINAL field names)
    """
    base_props_file = schema_dir / BASE_PROPERTIES_FILENAME
    properties: Dict[str, Any] = {}
    required_fields: Set[str] = set()

    if not base_props_file.is_file():
        logging.error(f"{BASE_PROPERTIES_FILENAME} not found in {schema_dir}. Cannot generate BaseElement.")
        return properties, required_fields

    try:
        with open(base_props_file, 'r', encoding='utf-8') as f:
            schema = yaml.safe_load(f)
    except Exception as e:
        logging.error(f"Error reading or parsing {base_props_file}: {e}")
        return properties, required_fields

    if not isinstance(schema, dict):
        logging.error(f"Invalid format in {base_props_file}. Root should be an object.")
        return properties, required_fields

    properties = schema.get("properties", {})
    # Store required fields using their original names from the YAML
    required_fields = {str(req) for req in schema.get("required", []) if isinstance(req, (str, int, float))}

    return properties, required_fields

def generate_base_element_cs(output_dir: Path, base_properties: Dict[str, Any], required_base_fields_original: Set[str]):
    """Generates the BaseElement.cs file from parsed base properties."""
    output_file = output_dir / "BaseElement.cs" # PascalCase filename
    logging.info(f"Generating {output_file}...")

    cs_lines = [
        "using System;",
        "using System.Collections.Generic;", # Needed for potential List<>
        "",
        "[System.Serializable]",
        "public class BaseElement",
        "{"
    ]
    processed_fields = set()
    needs_list_using = False

    for field_name_original, prop_details in base_properties.items():
        if not isinstance(prop_details, dict):
            logging.warning(f"Skipping invalid property format for '{field_name_original}' in base properties.")
            continue

        is_required = field_name_original in required_base_fields_original
        cs_type, cs_field_name, is_list = map_yaml_type_to_csharp(prop_details, field_name_original, is_required)

        if is_list:
            needs_list_using = True

        if cs_field_name not in processed_fields:
             field_line = f"    public {cs_type} {cs_field_name};"
             if is_list:
                  field_line += f" = new {cs_type}();" # Initialize lists
             cs_lines.append(field_line)
             processed_fields.add(cs_field_name)

    cs_lines.append("}")
    content = "\n".join(cs_lines) + "\n"

    # Adjust using statements based on need
    if not needs_list_using:
        content = content.replace("using System.Collections.Generic;\n", "")

    try:
        output_file.parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(content)
        logging.info(f"Successfully generated {output_file}")
    except IOError as e:
        logging.error(f"Failed to write {output_file}: {e}")

def process_properties_cs(properties_dict: Dict[str, Any], required_fields_original: Set[str], base_field_names: Set[str]) -> Tuple[List[str], bool]:
    """Processes a dictionary of properties and returns generated C# field lines and whether List<> is used."""
    cs_lines = []
    needs_list = False
    for field_name_original, prop_details in properties_dict.items():
        if not isinstance(prop_details, dict):
            logging.warning(f"Skipping invalid property format for '{field_name_original}'.")
            continue

        # Map type and get final field name
        is_required = field_name_original in required_fields_original
        cs_type, final_cs_field_name, is_list = map_yaml_type_to_csharp(prop_details, field_name_original, is_required)

        if is_list:
            needs_list = True

        # Skip base fields - they are inherited (unless it's World, handled outside)
        if final_cs_field_name in base_field_names:
            continue

        field_line = f"    public {cs_type} {final_cs_field_name};"
        if is_list:
             field_line += f" = new {cs_type}();" # Initialize lists

        cs_lines.append(field_line)
    return cs_lines, needs_list

def generate_cs_from_yaml(yaml_file: Path, output_dir: Path, base_field_names_pascal: Set[str]):
    """Generates a C# class file from a specific element YAML schema file."""
    if yaml_file.name == BASE_PROPERTIES_FILENAME:
        logging.info(f"Skipping base properties file: {yaml_file}")
        return

    try:
        with open(yaml_file, 'r', encoding='utf-8') as f:
            schema = yaml.safe_load(f)
    except yaml.YAMLError as e:
        logging.error(f"Error parsing YAML file {yaml_file}: {e}")
        return
    except IOError as e:
        logging.error(f"Error reading YAML file {yaml_file}: {e}")
        return

    if not isinstance(schema, dict) or "title" not in schema:
        logging.warning(f"Skipping invalid schema file: {yaml_file}. Missing 'title'.")
        return

    class_name = to_pascal_case(schema["title"].replace(" ", ""))
    output_file = output_dir / f"{class_name}.cs"
    logging.info(f"Processing {yaml_file} -> {output_file}...")

    # --- Class Definition --- 
    all_field_lines: List[str] = [] 
    needs_list_using = False
    
    # Special case for World - does not inherit BaseElement
    inherits = True
    if class_name == "World":
         inherits = False
         effective_base_fields = set() # World doesn't inherit anything
    else:
         effective_base_fields = base_field_names_pascal

    # --- Process Properties --- 
    schema_properties = schema.get("properties", {})
    if not isinstance(schema_properties, dict):
        logging.warning(f"Skipping invalid schema file: {yaml_file}. 'properties' is not an object.")
        schema_properties = {}
        
    # Get required fields specific to this element schema (using original names)
    element_required_list = schema.get("required", [])
    element_required_original = {str(req) for req in element_required_list if isinstance(req, (str, int, float))}

    # Check structure: direct properties or nested sections?
    is_nested_structure = all(isinstance(v, dict) and v.get("type") == "object" and "properties" in v for v in schema_properties.values())
    
    if not is_nested_structure or class_name == "World": 
        logging.debug(f"Processing {class_name} with direct properties structure.")
        field_lines, needs_list = process_properties_cs(schema_properties, element_required_original, effective_base_fields)
        all_field_lines.extend(field_lines)
        if needs_list:
             needs_list_using = True
    else:
        logging.debug(f"Processing {class_name} with nested section structure.")
        for section_name, section_details in schema_properties.items():
            if isinstance(section_details, dict) and "properties" in section_details:
                actual_section_properties = section_details.get("properties", {})
                if not isinstance(actual_section_properties, dict):
                    logging.warning(f"Skipping section '{section_name}' in {yaml_file}: inner 'properties' is not a dictionary.")
                    continue
                    
                section_required_list = section_details.get("required", [])
                section_required_original = {str(req) for req in section_required_list if isinstance(req, (str, int, float))}
                combined_required = element_required_original.union(section_required_original)
                
                # Add comment for section
                all_field_lines.append(f"    // {to_pascal_case(section_name)}") 
                field_lines, needs_list = process_properties_cs(actual_section_properties, combined_required, effective_base_fields)
                all_field_lines.extend(field_lines)
                if needs_list:
                     needs_list_using = True
            else:
                 logging.warning(f"Skipping item '{section_name}' in {yaml_file}. Expected a section object with a 'properties' key.")

    # --- Assemble File Content --- 
    cs_lines = [
        "using System;",
        "using System.Collections.Generic;" if needs_list_using else "", # Conditionally add using
        "",
        "[System.Serializable]",
    ]
    class_def = f"public class {class_name}"
    if inherits:
        class_def += " : BaseElement"
    cs_lines.append(class_def)
    cs_lines.append("{")
    cs_lines.extend(all_field_lines) # Add the generated field lines
    cs_lines.append("}")
    
    # Filter out empty using line if list wasn't needed
    cs_lines = [line for line in cs_lines if line]
    ts_content = "\n".join(cs_lines) + "\n"

    # --- Write File --- 
    try:
        output_file.parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(ts_content)
        logging.info(f"Successfully generated {output_file}")
    except IOError as e:
        logging.error(f"Failed to write {output_file}: {e}")

# --- Main Execution ---

def main():
    script_dir = Path(__file__).parent
    workspace_root = script_dir.parent
    schema_dir = workspace_root / "schema"
    # Define C# output directory
    output_dir = workspace_root / "conversions" / "csharp_unity"

    logging.info(f"Workspace root determined as: {workspace_root}")
    logging.info(f"Scanning for YAML schemas in: {schema_dir}")
    logging.info(f"C# Output directory set to: {output_dir}")

    if not schema_dir.is_dir():
        logging.error(f"Schema directory not found: {schema_dir}")
        return

    # 1. Parse base properties first (get original required names)
    base_properties, required_base_fields_original = parse_base_properties(schema_dir)
    if not base_properties:
        logging.error("Could not parse base properties. Aborting.")
        return

    # Derive set of base field names (PascalCase) for skipping inheritance
    base_field_names_pascal = set()
    for field_name_original in base_properties.keys():
        prop_details = base_properties.get(field_name_original, {})
        if isinstance(prop_details, dict):
             # Need to determine required status for correct mapping
             is_req = field_name_original in required_base_fields_original
             _, cs_field_name, _ = map_yaml_type_to_csharp(prop_details, field_name_original, is_req)
             base_field_names_pascal.add(cs_field_name)
        else:
             logging.warning(f"Skipping base property '{field_name_original}' due to invalid format.")

    # Ensure output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)

    # 2. Generate the base elements file
    generate_base_element_cs(output_dir, base_properties, required_base_fields_original)

    # 3. Process each specific YAML file in the schema directory
    yaml_files_found = False
    for item in schema_dir.iterdir():
        if item.is_file() and item.suffix.lower() == ".yaml":
            yaml_files_found = True
            # Pass the set of PascalCase base field names to skip inheritance
            generate_cs_from_yaml(item, output_dir, base_field_names_pascal)

    if not yaml_files_found:
         logging.warning(f"No YAML files found in {schema_dir} (excluding base properties).")
    else:
         logging.info("C# (Unity POCO) generation process completed.")

if __name__ == "__main__":
    main() 