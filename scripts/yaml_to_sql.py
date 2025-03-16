import os
import yaml

def generate_sql(base_properties, yaml_content, sql_path, is_world=False):
    with open(sql_path, 'w') as sql_file:
        # Handle the World schema differently
        if is_world:
            table_name = "world"
            sql_file.write(f"CREATE TABLE {table_name} (\n")
            
            # Extract fields directly from the World schema
            world_properties = list(yaml_content['World'].items())
            fields = []
            
            for field, field_type in world_properties:
                # Skip fields that are lists or complex types with descriptions
                if isinstance(field_type, dict) and 'type' in field_type and field_type['type'] == 'List':
                    # For list types, we'll create a separate table or use JSON storage
                    # Here we store it as TEXT which could be JSON formatted
                    fields.append(f"    {field.lower()} TEXT")
                    continue
                
                # Handle basic types
                if field_type == 'UUID' or field_type == 'String' or 'URL' in field_type:
                    sql_type = 'TEXT'
                elif field_type == 'Integer':
                    sql_type = 'INTEGER'
                elif isinstance(field_type, str) and '|' in field_type and 'Null' in field_type:
                    # Handle nullable types (e.g., "String | Null")
                    base_type = field_type.split('|')[0].strip()
                    if base_type == 'String' or base_type == 'URL':
                        sql_type = 'TEXT'
                    elif base_type == 'Integer':
                        sql_type = 'INTEGER'
                    else:
                        sql_type = 'TEXT'  # Default to TEXT for unknown types
                else:
                    sql_type = 'TEXT'  # Default to TEXT
                
                fields.append(f"    {field.lower()} {sql_type}")
            
            sql_file.write(",\n".join(fields))
        else:
            # Original logic for other schemas
            # Provide a default table name if 'title' is not available
            table_name = yaml_content.get('title', 'default_table_name').replace(" ", "_").lower()
            sql_file.write(f"CREATE TABLE {table_name} (\n")
            
            # First, write the SQL fields for 'Base' properties
            base_fields = []
            for field, details in base_properties.items():
                sql_type = 'TEXT' if details.get('type', 'string') == 'string' else 'INTEGER'
                base_fields.append(f"    {field.lower()} {sql_type}")
            sql_file.write(",\n".join(base_fields))
            
            if 'properties' in yaml_content:
                # Then write other properties from the category
                category_fields = []
                for section, section_content in yaml_content['properties'].items():
                    for field, details in section_content.get('properties', {}).items():
                        field_type = details.get('type', 'text')
                        sql_type = 'INTEGER' if field_type == 'integer' else 'TEXT'
                        category_fields.append(f"    {field.lower()} {sql_type}")
                if category_fields:
                    sql_file.write(",\n" + ",\n".join(category_fields))
        
        sql_file.write("\n);")
        
        # For World schema with list types, create additional tables
        if is_world:
            # Example: Create a table for time_format_equivalents
            if 'time_format_equivalents' in yaml_content['World']:
                sql_file.write("\n\n")
                sql_file.write("CREATE TABLE world_time_format_equivalents (\n")
                sql_file.write("    world_id TEXT,\n")
                sql_file.write("    position INTEGER,\n")
                sql_file.write("    value TEXT,\n")
                sql_file.write("    PRIMARY KEY (world_id, position),\n")
                sql_file.write("    FOREIGN KEY (world_id) REFERENCES world(id)\n")
                sql_file.write(");")
            
            # Create a table for time_format_names
            if 'time_format_names' in yaml_content['World']:
                sql_file.write("\n\n")
                sql_file.write("CREATE TABLE world_time_format_names (\n")
                sql_file.write("    world_id TEXT,\n")
                sql_file.write("    position INTEGER,\n")
                sql_file.write("    value TEXT,\n")
                sql_file.write("    PRIMARY KEY (world_id, position),\n")
                sql_file.write("    FOREIGN KEY (world_id) REFERENCES world(id)\n")
                sql_file.write(");")

def convert_yaml_to_sql(base_properties, yaml_path, sql_path):
    with open(yaml_path, 'r') as yaml_file:
        yaml_content = yaml.safe_load(yaml_file)
    
    # Check if this is the world.yaml file
    filename = os.path.basename(yaml_path)
    is_world = filename == 'world.yaml'
    
    generate_sql(base_properties, yaml_content, sql_path, is_world)

if __name__ == "__main__":
    script_directory = os.path.dirname(__file__)
    yaml_dir = os.path.join(script_directory, '..', 'schema')
    sql_dir = os.path.join(script_directory, '..', 'languages', 'sql')
    base_path = os.path.join(yaml_dir, 'base_properties.yaml')

    # Load base properties once
    with open(base_path, 'r') as file:
        base_properties = yaml.safe_load(file)['properties']

    os.makedirs(sql_dir, exist_ok=True)

    for filename in os.listdir(yaml_dir):
        if filename.endswith('.yaml') and filename != 'base_properties.yaml':
            yaml_path = os.path.join(yaml_dir, filename)
            sql_filename = filename[:-5].capitalize() + '.sql'
            sql_path = os.path.join(sql_dir, sql_filename)
            convert_yaml_to_sql(base_properties, yaml_path, sql_path)
            print(f"Converted {filename} to SQL: {sql_filename}")
