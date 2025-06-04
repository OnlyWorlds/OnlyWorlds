import os
import yaml

def get_sql_type_from_yaml_type(yaml_type):
    """Determine SQL type from YAML type."""
    if isinstance(yaml_type, dict):
        if 'type' in yaml_type:
            if yaml_type['type'] in ['string', 'multi-link', 'single-link', 'UUID', 'URL']:
                return 'TEXT'
            elif yaml_type['type'] == 'integer':
                return 'INTEGER'
            elif yaml_type['type'] == 'boolean':
                return 'BOOLEAN'
            elif yaml_type['type'] == 'number':
                return 'REAL'
            elif yaml_type['type'] == 'List' or yaml_type['type'] == 'array':
                return 'TEXT'  # Store lists/arrays as JSON text
    elif isinstance(yaml_type, str):
        if yaml_type in ['String', 'UUID', 'URL']:
            return 'TEXT'
        elif yaml_type == 'Integer':
            return 'INTEGER'
        elif yaml_type == 'Boolean':
            return 'BOOLEAN'
        elif yaml_type == 'Number':
            return 'REAL'
        elif '|' in yaml_type and 'None' in yaml_type:
            base_type = yaml_type.split('|')[0].strip()
            return get_sql_type_from_yaml_type(base_type)
    
    return 'TEXT'  # Default to TEXT for unknown types

def extract_fields_from_yaml(yaml_data, is_world=False):
    """Extract field definitions from YAML data."""
    fields = []
    
    # Handle the World schema
    if is_world and 'World' in yaml_data:
        for field, field_type in yaml_data['World'].items():
            sql_type = get_sql_type_from_yaml_type(field_type)
            fields.append((field.lower(), sql_type))
    # Handle schemas with 'properties' structure
    elif 'properties' in yaml_data:
        for section, section_data in yaml_data['properties'].items():
            if isinstance(section_data, dict) and 'properties' in section_data:
                for field, field_details in section_data['properties'].items():
                    sql_type = get_sql_type_from_yaml_type(field_details)
                    fields.append((field.lower(), sql_type))
    
    return fields

def generate_sql_table(table_name, fields):
    """Generate SQL CREATE TABLE statement."""
    sql = f"CREATE TABLE {table_name} (\n"
    field_definitions = [f"    {field} {sql_type}" for field, sql_type in fields]
    sql += ",\n".join(field_definitions)
    sql += "\n);"
    return sql

def generate_related_tables(main_table, yaml_data):
    """Generate related tables for list fields."""
    related_tables = []
    
    if 'World' in yaml_data:
        for field, field_type in yaml_data['World'].items():
            if isinstance(field_type, dict) and 'type' in field_type and field_type['type'] == 'List':
                table_name = f"{main_table}_{field.lower()}"
                sql = f"CREATE TABLE {table_name} (\n"
                sql += f"    {main_table}_id TEXT,\n"
                sql += "    position INTEGER,\n"
                sql += "    value TEXT,\n"
                sql += f"    PRIMARY KEY ({main_table}_id, position),\n"
                sql += f"    FOREIGN KEY ({main_table}_id) REFERENCES {main_table}(id)\n"
                sql += ");"
                related_tables.append(sql)
    
    return related_tables

def generate_element_sql(element_yaml_data, base_yaml_data, sql_path):
    """Generate SQL schema for an element, including base props and respecting required fields."""
    if not element_yaml_data:
        print(f"Error: Invalid YAML data for {os.path.basename(sql_path)}")
        return
        
    table_name = os.path.basename(sql_path).replace('.sql', '').lower()

    all_fields_sql = []
    required_base_fields = base_yaml_data.get('required', [])

    for field, details in base_yaml_data.get('properties', {}).items():
        field_name_lower = field.lower()
        sql_type = get_sql_type_from_yaml_type(details)
        not_null_constraint = " NOT NULL" if field in required_base_fields else ""
        if field_name_lower == 'id':
            not_null_constraint = " NOT NULL PRIMARY KEY"
        all_fields_sql.append(f"    {field_name_lower} {sql_type}{not_null_constraint}")

    if 'properties' in element_yaml_data:
        for section, section_content in element_yaml_data['properties'].items():
            if isinstance(section_content, dict) and 'properties' in section_content:
                nested_properties = section_content.get('properties', {})
                nested_required_fields = section_content.get('required', [])

                for field, details in nested_properties.items():
                    field_name_lower = field.lower()
                    sql_type = get_sql_type_from_yaml_type(details)
                    not_null_constraint = " NOT NULL" if field in nested_required_fields else ""
                    all_fields_sql.append(f"    {field_name_lower} {sql_type}{not_null_constraint}")

    with open(sql_path, 'w') as sql_file:
        sql_file.write(f"CREATE TABLE {table_name} (\n")
        if all_fields_sql:
            sql_file.write(",\n".join(all_fields_sql))
        else:
            sql_file.write("    -- No fields defined")
        sql_file.write("\n);")

def convert_yaml_to_sql(yaml_path, sql_path):
    """Convert YAML file to SQL schema without base properties."""
    with open(yaml_path, 'r') as yaml_file:
        yaml_content = yaml.safe_load(yaml_file)
    generate_element_sql(yaml_content, yaml_content.get('properties', {}), sql_path)

def load_yaml_data(yaml_path):
    try:
        with open(yaml_path, 'r', encoding='utf-8') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        print(f"Error: YAML file not found at {yaml_path}")
        return None
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file {yaml_path}: {e}")
        return None

if __name__ == "__main__":
    script_directory = os.path.dirname(__file__)
    yaml_dir = os.path.join(script_directory, '..', 'schema')
    sql_dir = os.path.join(script_directory, '..', 'languages', 'sql')
    base_path = os.path.join(yaml_dir, 'base_properties.yaml')

    # Load full base properties data once (including required fields)
    base_yaml_data = load_yaml_data(base_path)
    if not base_yaml_data:
        print("Fatal Error: Could not load base_properties.yaml. Exiting.")
        exit(1)

    # Ensure output directory exists
    os.makedirs(sql_dir, exist_ok=True)

    # Convert all YAML files to SQL, now including base properties and NOT NULL constraints
    for filename in os.listdir(yaml_dir):
        if filename.endswith('.yaml') and filename != 'base_properties.yaml':
            yaml_path = os.path.join(yaml_dir, filename)
            sql_filename = filename[:-5].capitalize() + '.sql' # Keep existing naming
            sql_path = os.path.join(sql_dir, sql_filename)
            
            element_yaml_data = load_yaml_data(yaml_path)
            if element_yaml_data:
                 # Pass both element data and the correct base_yaml_data
                generate_element_sql(element_yaml_data, base_yaml_data, sql_path)
                print(f"Generated SQL for {filename}: {sql_filename}")
            else:
                 print(f"Skipped SQL generation for {filename} due to load error.")
