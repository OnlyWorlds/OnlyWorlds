import os
import yaml
import re
import logging
from pathlib import Path
from typing import Tuple, Dict, Any, Set, List

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# --- Constants ---
BASE_PROPERTIES_FILENAME = "base_properties.yaml"
CSHARP_KEYWORDS = {"class", "event", "object", "string", "int", "bool", "public", "private", "protected", "static", "namespace", "using", "base", "new"}
KEYWORD_PREFIX = "tt_" # Prefix for C# keywords used as field names

# --- Helper Functions ---

def to_pascal_case(snake_str):
    """Converts various cases to PascalCase."""
    if not snake_str:
        return ""
    components = re.split('_|-|(?=[A-Z])', snake_str)
    return ''.join(x.capitalize() for x in components if x)

def to_csharp_fieldname(original_name):
    """Converts YAML name to lowercase C# field name, handling keywords."""
    # First, convert to a base form (e.g., camelCase) to handle separators
    camel_case = original_name
    if '_' in camel_case or '-' in camel_case:
        components = re.split('_|-', camel_case)
        camel_case = components[0] + ''.join(x.title() for x in components[1:])
    # Ensure first letter is lowercase
    field_name = camel_case[0].lower() + camel_case[1:]
    # Prefix if it's a keyword
    if field_name in CSHARP_KEYWORDS:
        return KEYWORD_PREFIX + field_name
    return field_name

def map_yaml_to_csharp_unity_json_properties(yaml_prop: Dict[str, Any], field_name_original: str) -> Tuple[str, List[str]]:
    """Maps YAML type properties to C# type string and attribute strings for the advanced Unity format."""
    yaml_type = yaml_prop.get("type")
    category = yaml_prop.get("category", "Element") # Default category if missing
    maximum = yaml_prop.get("maximum")
    
    cs_type = "object" # Default fallback
    attributes = [f'[JsonProperty("{field_name_original}")]'] # Always add JsonProperty
    
    # Determine C# type and custom attribute based on YAML type
    if yaml_type == "string":
        cs_type = "string"
        attributes.append('[TextAttribute("")]')
    elif yaml_type == "integer":
        cs_type = "int"
        max_val = maximum if isinstance(maximum, int) else 0
        attributes.append(f"[Integer({max_val})]")
    elif yaml_type == "boolean":
        cs_type = "bool"
        # No specific attribute in Character.cs example, maybe add [BooleanAttribute] later?
    elif yaml_type == "array":
        # Map arrays to string based on Character.cs pattern (avoiding List<>)
        cs_type = "string"
        attributes.append('[TextAttribute("")]') # Treat same as string for now
        logging.warning(f"YAML array field '{field_name_original}' mapped to C# string. Review if List<> or custom handling needed.")
    elif yaml_type == "single-link":
        cs_type = "string"
        ref_type = to_pascal_case(category)
        attributes.append(f"[ReferenceAttribute(typeof({ref_type}))]")
    elif yaml_type == "multi-link":
        cs_type = "string"
        ref_type = to_pascal_case(category)
        attributes.append(f"[ReferenceAttribute(typeof({ref_type}), true)]") # isList = true
    elif yaml_type == "generic-link":
         cs_type = "string"
         # Use Element as default type, assuming it's the base for most linkable things
         attributes.append(f"[ReferenceAttribute(typeof(Element))]") 
    else:
        if yaml_type not in ["object"]:
             logging.warning(f"Unknown YAML type '{yaml_type}' for field '{field_name_original}'. Defaulting to C# 'object'.")

    return cs_type, attributes

def parse_base_properties(schema_dir: Path) -> Tuple[Dict[str, Any], Set[str]]:
    """Parses the base_properties.yaml file. Returns properties and required ORIGINAL names."""
    # This function is the same as in the POCO script
    base_props_file = schema_dir / BASE_PROPERTIES_FILENAME
    properties: Dict[str, Any] = {}
    required_fields: Set[str] = set()
    if not base_props_file.is_file():
        logging.error(f"{BASE_PROPERTIES_FILENAME} not found in {schema_dir}. Cannot generate Element.")
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
    required_fields = {str(req) for req in schema.get("required", []) if isinstance(req, (str, int, float))}
    return properties, required_fields

def generate_base_element_cs_unity_json(output_dir: Path, base_properties: Dict[str, Any], required_base_fields_original: Set[str]):
    """Generates the Element.cs file using the advanced Unity/JSON format."""
    class_name = "Element" # Match Character.cs base
    output_file = output_dir / f"{class_name}.cs"
    logging.info(f"Generating {output_file}...")

    cs_lines = [
        "using System;",
        "using System.Collections.Generic;",
        "using Newtonsoft.Json;",
        "using Utils;", # Assuming custom attributes are in Utils namespace
        "",
        "[System.Serializable]",
        f"public class {class_name}", # No inheritance for the base itself
        "{"
    ]
    processed_fields = set()

    for field_name_original, prop_details in base_properties.items():
        if not isinstance(prop_details, dict):
            logging.warning(f"Skipping invalid property format for '{field_name_original}' in base properties.")
            continue

        cs_fieldname = to_csharp_fieldname(field_name_original)
        cs_type, attributes = map_yaml_to_csharp_unity_json_properties(prop_details, field_name_original)
        
        # Handle WorldId special case if 'world' is in base props
        if field_name_original.lower() == "world":
            cs_fieldname = "worldId"
            # Recalculate attributes/type for WorldId (it's just a string ID, likely required)
            cs_type = "string"
            attributes = [f'[JsonProperty("{field_name_original}")]'] # Keep original name in JsonProperty
            # Determine if 'World' was required in base_properties.yaml
            # if field_name_original in required_base_fields_original: # Add non-null check if needed
            #     attributes.append("[NonNull]") # Example if using non-null attr

        if cs_fieldname not in processed_fields:
             # Combine attributes onto a single line
             if attributes:
                 # Remove brackets from individual attributes before joining
                 cleaned_attrs = [a.strip()[1:-1] for a in attributes]
                 combined_attrs_line = f"    [{', '.join(cleaned_attrs)}]"
                 cs_lines.append(combined_attrs_line)
             # Add field declaration (lowercase)
             cs_lines.append(f"    public {cs_type} {cs_fieldname};")
             processed_fields.add(cs_fieldname)

    cs_lines.append("}")
    content = "\n".join(cs_lines).rstrip() + "\n" # Clean trailing blank lines before final newline

    try:
        output_file.parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(content)
        logging.info(f"Successfully generated {output_file}")
    except IOError as e:
        logging.error(f"Failed to write {output_file}: {e}")

def process_properties_cs_unity_json(properties_dict: Dict[str, Any], required_fields_original: Set[str], base_field_names_lower: Set[str]) -> List[str]:
    """Processes properties dict and returns C# lines for the advanced format."""
    cs_lines = []
    for field_name_original, prop_details in properties_dict.items():
        if not isinstance(prop_details, dict):
            logging.warning(f"Skipping invalid property format for '{field_name_original}'.")
            continue

        cs_fieldname = to_csharp_fieldname(field_name_original)

        # Skip base fields - they are inherited (unless it's World, handled outside)
        if cs_fieldname in base_field_names_lower:
            continue
            
        cs_type, attributes = map_yaml_to_csharp_unity_json_properties(prop_details, field_name_original)

        # Combine attributes onto a single line
        if attributes:
            # Remove brackets from individual attributes before joining
            cleaned_attrs = [a.strip()[1:-1] for a in attributes]
            combined_attrs_line = f"    [{', '.join(cleaned_attrs)}]"
            cs_lines.append(combined_attrs_line)
        # Add field declaration (lowercase)
        cs_lines.append(f"    public {cs_type} {cs_fieldname};")
        
    return cs_lines

def generate_cs_unity_json_from_yaml(yaml_file: Path, output_dir: Path, base_field_names_lower: Set[str]):
    """Generates a C# class file using the advanced Unity/JSON format."""
    if yaml_file.name == BASE_PROPERTIES_FILENAME:
        return # Skip base file

    try:
        with open(yaml_file, 'r', encoding='utf-8') as f:
            schema = yaml.safe_load(f)
    except Exception as e:
        logging.error(f"Error reading/parsing YAML file {yaml_file}: {e}")
        return

    if not isinstance(schema, dict) or "title" not in schema:
        logging.warning(f"Skipping invalid schema file: {yaml_file}. Missing 'title'.")
        return

    class_name = to_pascal_case(schema["title"].replace(" ", ""))
    output_file = output_dir / f"{class_name}.cs"
    logging.info(f"Processing {yaml_file} -> {output_file}...")

    # --- Class Definition --- 
    all_field_lines: List[str] = [] 
    
    inherits = True
    effective_base_fields = base_field_names_lower
    if class_name == "World":
         inherits = False
         effective_base_fields = set()

    # --- Process Properties --- 
    schema_properties = schema.get("properties", {})
    if not isinstance(schema_properties, dict):
        logging.warning(f"Skipping invalid schema file: {yaml_file}. 'properties' is not an object.")
        schema_properties = {}
        
    element_required_list = schema.get("required", [])
    element_required_original = {str(req) for req in element_required_list if isinstance(req, (str, int, float))}

    # Check structure: direct properties or nested sections?
    is_nested_structure = all(isinstance(v, dict) and v.get("type") == "object" and "properties" in v for v in schema_properties.values()) 
    
    if not is_nested_structure or class_name == "World": 
        logging.debug(f"Processing {class_name} with direct properties structure.")
        field_lines = process_properties_cs_unity_json(schema_properties, element_required_original, effective_base_fields)
        all_field_lines.extend(field_lines)
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
                
                # Add comment for section (optional)
                # all_field_lines.append(f"    // --- {to_pascal_case(section_name)} ---") 
                field_lines = process_properties_cs_unity_json(actual_section_properties, combined_required, effective_base_fields)
                all_field_lines.extend(field_lines)
            else:
                 logging.warning(f"Skipping item '{section_name}' in {yaml_file}. Expected a section object with a 'properties' key.")

    # --- Assemble File Content --- 
    cs_lines = [
        "using System;",
        "using System.Collections.Generic;",
        "using Newtonsoft.Json;",
        "using Utils;", # Assuming custom attributes are in Utils namespace
        "",
        "[System.Serializable]",
    ]
    class_def = f"public class {class_name}"
    if inherits:
        class_def += " : Element" # Inherit from Element
    cs_lines.append(class_def)
    cs_lines.append("{")
    cs_lines.extend(all_field_lines) # Add the generated field lines
    # Remove potential trailing blank line from last field
    if cs_lines[-1] == "": 
        cs_lines.pop()
    cs_lines.append("}")
    
    content = "\n".join(cs_lines) + "\n"

    # --- Write File --- 
    try:
        output_file.parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(content)
        logging.info(f"Successfully generated {output_file}")
    except IOError as e:
        logging.error(f"Failed to write {output_file}: {e}")

# --- Main Execution ---

def main():
    script_dir = Path(__file__).parent
    workspace_root = script_dir.parent
    schema_dir = workspace_root / "schema"
    output_dir = workspace_root / "conversions" / "csharp_unity_json_properties"

    logging.info(f"Workspace root determined as: {workspace_root}")
    logging.info(f"Scanning for YAML schemas in: {schema_dir}")
    logging.info(f"C# Advanced Properties Output directory set to: {output_dir}")

    if not schema_dir.is_dir():
        logging.error(f"Schema directory not found: {schema_dir}")
        return

    # 1. Parse base properties
    base_properties, required_base_fields_original = parse_base_properties(schema_dir)
    if not base_properties:
        logging.error("Could not parse base properties. Aborting.")
        return

    # Derive set of base field names (lowercase) for skipping inheritance
    base_field_names_lower = set()
    for field_name_original in base_properties.keys():
        prop_details = base_properties.get(field_name_original, {})
        if isinstance(prop_details, dict):
             cs_fieldname = to_csharp_fieldname(field_name_original)
             # Handle WorldId special case
             if field_name_original.lower() == "world":
                 cs_fieldname = "worldId"
             base_field_names_lower.add(cs_fieldname)
        else:
             logging.warning(f"Skipping base property '{field_name_original}' due to invalid format.")

    # Ensure output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)

    # 2. Generate the base element file (Element.cs)
    generate_base_element_cs_unity_json(output_dir, base_properties, required_base_fields_original)

    # 3. Process each specific YAML file
    yaml_files_found = False
    for item in schema_dir.iterdir():
        if item.is_file() and item.suffix.lower() == ".yaml":
            yaml_files_found = True
            generate_cs_unity_json_from_yaml(item, output_dir, base_field_names_lower)

    if not yaml_files_found:
         logging.warning(f"No YAML files found in {schema_dir} (excluding base properties).")
    else:
         logging.info("C# (Unity Advanced JSON) generation process completed.")
    
    logging.warning("Reminder: ReverseLookupAttributes cannot be inferred from schemas and must be added manually or via other means.")

if __name__ == "__main__":
    main() 