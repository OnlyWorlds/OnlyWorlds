CREATE TABLE world (
    id TEXT,
    api_key TEXT,
    name TEXT,
    description TEXT,
    version TEXT,
    image_url TEXT,
    time_format_equivalents TEXT,
    time_format_names TEXT,
    time_basic_unit TEXT,
    time_range_min INTEGER,
    time_range_max INTEGER,
    time_current INTEGER
);

CREATE TABLE world_time_format_equivalents (
    world_id TEXT,
    position INTEGER,
    value TEXT,
    PRIMARY KEY (world_id, position),
    FOREIGN KEY (world_id) REFERENCES world(id)
);

CREATE TABLE world_time_format_names (
    world_id TEXT,
    position INTEGER,
    value TEXT,
    PRIMARY KEY (world_id, position),
    FOREIGN KEY (world_id) REFERENCES world(id)
);