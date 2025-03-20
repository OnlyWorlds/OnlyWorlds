CREATE TABLE default_table_name (
    -- No properties defined
);

CREATE TABLE default_table_name_time_format_equivalents (
    default_table_name_id TEXT,
    position INTEGER,
    value TEXT,
    PRIMARY KEY (default_table_name_id, position),
    FOREIGN KEY (default_table_name_id) REFERENCES default_table_name(id)
);

CREATE TABLE default_table_name_time_format_names (
    default_table_name_id TEXT,
    position INTEGER,
    value TEXT,
    PRIMARY KEY (default_table_name_id, position),
    FOREIGN KEY (default_table_name_id) REFERENCES default_table_name(id)
);