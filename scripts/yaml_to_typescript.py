import os
import yaml
import re
import logging
from pathlib import Path
from typing import Tuple, Dict, Any, Set

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# --- Constants ---
BASE_PROPERTIES_FILENAME = "base_properties.yaml"

# --- Helper Functions ---

def to_camel_case(snake_str):
    """Converts snake_case, PascalCase or kebab-case to camelCase."""
    if not snake_str:
        return ""
    # Special case for names that are already camelCase or PascalCase but contain underscores/hyphens
    components = re.split('_|-', snake_str)
    # Make first letter of first component lowercase, capitalize first letter of subsequent components
    first_component = components[0]
    first_letter = first_component[0].lower()
    camel_case_name = first_letter + first_component[1:] + ''.join(x.title() for x in components[1:])
    return camel_case_name

def map_yaml_type_to_ts_basic(yaml_prop: Dict[str, Any], field_name_original: str) -> Tuple[str, str]:
    """Maps YAML type properties to basic TypeScript type and transformed field name."""
    yaml_type = yaml_prop.get("type")
    category = yaml_prop.get("category")
    ts_type = "any" # Default fallback
    original_camel_case_name = to_camel_case(field_name_original)
    ts_field_name = original_camel_case_name # Start with camelCase

    if yaml_type == "string":
        ts_type = "string"
    elif yaml_type == "integer":
        ts_type = "number"
    elif yaml_type == "boolean":
        ts_type = "boolean"
    elif yaml_type == "array":
        # Basic array handling, assumes simple items type
        items_prop = yaml_prop.get("items", {})
        item_type, _ = map_yaml_type_to_ts_basic(items_prop, "") # Get basic type for items
        ts_type = f"{item_type}[]"
    elif yaml_type == "single-link":
        ts_type = "string" # Represent link by ID
        # Special handling for 'World' -> 'worldId'
        if field_name_original.lower() == "world":
             ts_field_name = "worldId"
        else:
             ts_field_name = original_camel_case_name + "Id"
        if not category and field_name_original.lower() != "world":
            logging.warning(f"Field '{field_name_original}' is single-link but has no category.")
    elif yaml_type == "multi-link":
        ts_type = "string[]" # Array of IDs
        ts_field_name = original_camel_case_name + "Ids"
        if not category:
            logging.warning(f"Field '{field_name_original}' is multi-link but has no category.")
    elif yaml_type == "generic-link": # Handle generic-link like single-link
         ts_type = "string"
         ts_field_name = original_camel_case_name + "Id"
         # Note: We might need content_type field as well, but keeping it simple for now
    else:
        # Allow passthrough for types like "object" if needed, but log others
        if yaml_type not in ["object"]:
             logging.warning(f"Unknown YAML type '{yaml_type}' for field '{field_name_original}'. Defaulting to 'any'.")

    return ts_type, ts_field_name

def parse_base_properties(schema_dir: Path) -> Tuple[Dict[str, Any], Set[str]]:
    """Parses the base_properties.yaml file."

    Returns:
        A tuple containing: (properties dictionary, set of required camelCase field names)
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
    required_list = schema.get("required", [])

    # Convert required list to a set of camelCase names for easier lookup
    # Handle 'World' -> 'worldId' specifically
    for req_field in required_list:
        if req_field.lower() == "world":
             required_fields.add("worldId")
        else:
             # Use original field name from required list for the check
             required_fields.add(to_camel_case(req_field))

    return properties, required_fields

def generate_base_elements_ts(output_dir: Path, base_properties: Dict[str, Any], required_base_fields: Set[str]):
    """Generates the base_elements.ts file from parsed base properties."""
    output_file = output_dir / "base_elements.ts"
    logging.info(f"Generating {output_file}...")

    content_lines = ["// Base interface for all world elements (Generated from base_properties.yaml)", "export interface BaseElement {"]
    processed_fields = set()

    for field_name_original, prop_details in base_properties.items():
        if not isinstance(prop_details, dict):
            logging.warning(f"Skipping invalid property format for '{field_name_original}' in base properties.")
            continue

        # Get basic type and potentially transformed name (e.g., worldId)
        ts_type, ts_field_name = map_yaml_type_to_ts_basic(prop_details, field_name_original)

        # Determine if required based on the original name listed in base_properties.yaml required list
        is_required = to_camel_case(field_name_original) in required_base_fields

        # Construct final type string
        if is_required:
            final_type_str = f": {ts_type};"
        else:
            final_type_str = f"?: {ts_type} | null;"

        if ts_field_name not in processed_fields:
             # Removed JSDoc comment generation
             content_lines.append(f"  {ts_field_name}{final_type_str}")
             processed_fields.add(ts_field_name)

    content_lines.append("}")
    content = "\n".join(content_lines) + "\n"

    try:
        output_file.parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(content)
        logging.info(f"Successfully generated {output_file}")
    except IOError as e:
        logging.error(f"Failed to write {output_file}: {e}")

def process_properties(properties_dict: Dict[str, Any], required_fields_original: Set[str], base_field_names: Set[str]) -> list[str]:
    """Processes a dictionary of properties and returns generated TS lines."""
    ts_lines = []
    for field_name_original, prop_details in properties_dict.items():
        if not isinstance(prop_details, dict):
            logging.warning(f"Skipping invalid property format for '{field_name_original}'.")
            continue

        # Map type and get final field name (e.g., systemId)
        ts_type, final_ts_field_name = map_yaml_type_to_ts_basic(prop_details, field_name_original)

        # Skip base fields - they are inherited from BaseElement (unless it's World)
        if final_ts_field_name in base_field_names:
            continue

        # Determine if required based on the *original* field name in the element's required list
        is_required = field_name_original in required_fields_original
        if is_required:
            final_type_str = f": {ts_type};"
        else:
            final_type_str = f"?: {ts_type} | null;"

        # Removed JSDoc comment generation
        ts_lines.append(f"  {final_ts_field_name}{final_type_str}")
    return ts_lines

def generate_ts_from_yaml(yaml_file: Path, output_dir: Path, base_field_names: Set[str]):
    """Generates a TypeScript interface file from a specific element YAML schema file."""
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

    interface_name = schema["title"].replace(" ", "")
    output_file = output_dir / f"{interface_name}.ts"
    logging.info(f"Processing {yaml_file} -> {output_file}...")

    # --- Interface Definition --- 
    # Special case for World - does not extend BaseElement
    if interface_name == "World":
         ts_lines = ["", f"export interface {interface_name} {{"]
         effective_base_fields = set() # World doesn't inherit anything
    else:
         ts_lines = [f"import {{ BaseElement }} from './base_elements';", ""]
         ts_lines.append(f"export interface {interface_name} extends BaseElement {{")
         effective_base_fields = base_field_names # Other elements inherit base fields

    # --- Process Properties --- 
    schema_properties = schema.get("properties", {})
    if not isinstance(schema_properties, dict):
        logging.warning(f"Skipping invalid schema file: {yaml_file}. 'properties' is not an object.")
        schema_properties = {}
        
    # Get required fields specific to this element schema (using original names)
    element_required_list = schema.get("required", [])
    element_required_original = {str(req) for req in element_required_list if isinstance(req, (str, int, float))}

    # Check structure: direct properties or nested sections?
    # A section typically has type "object" and its own "properties"
    is_nested_structure = all(isinstance(v, dict) and v.get("type") == "object" and "properties" in v for v in schema_properties.values())
    has_direct_properties = any(isinstance(v, dict) and 'type' in v and v.get("type") != "object" for v in schema_properties.values())
    
    # Heuristic: If all top-level properties are objects with their own properties, assume nested structure.
    # If there are direct properties (not type object) at the top level, assume direct structure (like World).
    # Handle mixed cases? For now, prefer nested if it looks like it.
    
    if not is_nested_structure or interface_name == "World": # Treat World as direct, or if structure isn't clearly nested
        # Process properties directly under schema["properties"]
        logging.debug(f"Processing {interface_name} with direct properties structure.")
        ts_lines.extend(process_properties(schema_properties, element_required_original, effective_base_fields))
    else:
        # Iterate through nested sections (like Ability, Character etc.)
        logging.debug(f"Processing {interface_name} with nested section structure.")
        for section_name, section_details in schema_properties.items():
            # Check if section_details is a dict and has 'properties'
            if isinstance(section_details, dict) and "properties" in section_details:
                actual_section_properties = section_details.get("properties", {})
                if not isinstance(actual_section_properties, dict):
                    logging.warning(f"Skipping section '{section_name}' in {yaml_file}: inner 'properties' is not a dictionary.")
                    continue
                    
                # Get required list specific to this section, if any
                section_required_list = section_details.get("required", [])
                section_required_original = {str(req) for req in section_required_list if isinstance(req, (str, int, float))}
                # Combine section required with top-level required for checking fields within this section
                # Note: This assumes required fields are listed at the section level if they apply only to that section.
                combined_required = element_required_original.union(section_required_original)
                
                ts_lines.append(f"  // {section_name}")
                # Process the ACTUAL properties within the section
                ts_lines.extend(process_properties(actual_section_properties, combined_required, effective_base_fields))
            else:
                 # Log if a top-level item doesn't look like a section object with properties
                 logging.warning(f"Skipping item '{section_name}' in {yaml_file}. Expected a section object with a 'properties' key.")

    ts_lines.append("}")
    ts_content = "\n".join(ts_lines) + "\n"

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
    output_dir = workspace_root / "languages" / "typescript"

    logging.info(f"Workspace root determined as: {workspace_root}")
    logging.info(f"Scanning for YAML schemas in: {schema_dir}")
    logging.info(f"Output directory set to: {output_dir}")

    if not schema_dir.is_dir():
        logging.error(f"Schema directory not found: {schema_dir}")
        return

    # 1. Parse base properties first
    base_properties, required_base_fields_orig_case = parse_base_properties(schema_dir)
    if not base_properties:
        logging.error("Could not parse base properties. Aborting.")
        return

    # Derive set of base field names (camelCase) for skipping in specific elements
    base_field_names_camel = set()
    for field_name_original in base_properties.keys():
        prop_details = base_properties.get(field_name_original, {})
        if isinstance(prop_details, dict):
             _, ts_field_name = map_yaml_type_to_ts_basic(prop_details, field_name_original)
             base_field_names_camel.add(ts_field_name)
        else:
             logging.warning(f"Skipping base property '{field_name_original}' due to invalid format.")


    # Ensure output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)

    # 2. Generate the base elements file (passing camelCase required names)
    # The generate_base_elements_ts function needs camelCase names for its check
    required_base_fields_camel = {to_camel_case(f) for f in required_base_fields_orig_case}
    generate_base_elements_ts(output_dir, base_properties, required_base_fields_camel)

    # 3. Process each specific YAML file in the schema directory
    yaml_files_found = False
    for item in schema_dir.iterdir():
        if item.is_file() and item.suffix.lower() == ".yaml":
            yaml_files_found = True
            # Pass the set of camelCase base field names to skip inheritance
            generate_ts_from_yaml(item, output_dir, base_field_names_camel)

    if not yaml_files_found:
         logging.warning(f"No YAML files found in {schema_dir} (excluding base properties).")
    else:
         logging.info("TypeScript generation process completed.")

if __name__ == "__main__":
    main() 