import os
import yaml

def get_sql_type_from_yaml_type(yaml_type):
    """Determine SQL type from YAML type."""
    if isinstance(yaml_type, dict):
        if 'type' in yaml_type:
            if yaml_type['type'] in ['string', 'multi-link', 'single-link']:
                return 'TEXT'
            elif yaml_type['type'] == 'integer':
                return 'INTEGER'
            elif yaml_type['type'] == 'List':
                return 'TEXT'  # Store lists as JSON text
    elif isinstance(yaml_type, str):
        if yaml_type in ['String', 'UUID', 'URL'] or 'URL' in yaml_type:
            return 'TEXT'
        elif yaml_type == 'Integer':
            return 'INTEGER'
        elif '|' in yaml_type and 'Null' in yaml_type:
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

def generate_base_properties_sql(base_properties, sql_path):
    """Generate a base properties SQL file."""
    with open(sql_path, 'w') as sql_file:
        sql_file.write("CREATE TABLE abstract_element (\n")
        
        # Write SQL fields for base properties
        base_fields = []
        for field, details in base_properties.items():
            sql_type = get_sql_type_from_yaml_type(details)
            base_fields.append(f"    {field.lower()} {sql_type}")
        sql_file.write(",\n".join(base_fields))
        
        sql_file.write("\n);")
    print(f"Generated base properties SQL")

def generate_element_sql(yaml_content, sql_path):
    """Generate SQL schema for an element without base properties."""
    with open(sql_path, 'w') as sql_file:
        # Get table name from the title or filename
        table_name = yaml_content.get('title', 'default_table_name').replace(" ", "_").lower()
        sql_file.write(f"CREATE TABLE {table_name} (\n")
        
        # Only include the element-specific properties, not base properties
        if 'properties' in yaml_content:
            category_fields = []
            for section, section_content in yaml_content['properties'].items():
                for field, details in section_content.get('properties', {}).items():
                    sql_type = get_sql_type_from_yaml_type(details)
                    category_fields.append(f"    {field.lower()} {sql_type}")
            if category_fields:
                sql_file.write(",\n".join(category_fields))
            else:
                # If no category-specific fields, add a placeholder comment
                sql_file.write("    -- No element-specific fields")
        else:
            # If no properties at all, add a placeholder comment
            sql_file.write("    -- No properties defined")
        
        sql_file.write("\n);")
        
        # Check if this is the world schema and add related tables if needed
        filename = os.path.basename(sql_path).lower()
        if "world.sql" in filename:
            related_tables = generate_related_tables(table_name, yaml_content)
            for related_table in related_tables:
                sql_file.write("\n\n")
                sql_file.write(related_table)

def convert_yaml_to_sql(yaml_path, sql_path):
    """Convert YAML file to SQL schema without base properties."""
    with open(yaml_path, 'r') as yaml_file:
        yaml_content = yaml.safe_load(yaml_file)
    generate_element_sql(yaml_content, sql_path)

if __name__ == "__main__":
    script_directory = os.path.dirname(__file__)
    yaml_dir = os.path.join(script_directory, '..', 'schema')
    sql_dir = os.path.join(script_directory, '..', 'conversions', 'sql')
    base_path = os.path.join(yaml_dir, 'base_properties.yaml')

    # Load base properties once
    with open(base_path, 'r') as file:
        base_properties = yaml.safe_load(file)['properties']

    # Ensure output directory exists
    os.makedirs(sql_dir, exist_ok=True)

    # Generate base properties SQL
    base_sql_path = os.path.join(sql_dir, 'abstract_element.sql')
    generate_base_properties_sql(base_properties, base_sql_path)

    # Convert all YAML files to SQL (without base properties)
    for filename in os.listdir(yaml_dir):
        if filename.endswith('.yaml') and filename != 'base_properties.yaml':
            yaml_path = os.path.join(yaml_dir, filename)
            sql_filename = filename[:-5].capitalize() + '.sql'
            sql_path = os.path.join(sql_dir, sql_filename)
            convert_yaml_to_sql(yaml_path, sql_path)
            print(f"Converted {filename} to SQL: {sql_filename}")
