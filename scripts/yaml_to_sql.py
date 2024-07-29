import os
import yaml

def generate_sql(base_properties, yaml_content, sql_path):
    with open(sql_path, 'w') as sql_file:
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

def convert_yaml_to_sql(base_properties, yaml_path, sql_path):
    with open(yaml_path, 'r') as yaml_file:
        yaml_content = yaml.safe_load(yaml_file)
    generate_sql(base_properties, yaml_content, sql_path)

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
