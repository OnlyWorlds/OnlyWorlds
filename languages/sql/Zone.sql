CREATE TABLE zone (
    id TEXT NOT NULL PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    supertype TEXT,
    subtype TEXT,
    image_url TEXT,
    world TEXT NOT NULL,
    role TEXT,
    start_date INTEGER,
    end_date INTEGER,
    phenomena TEXT,
    linked_zones TEXT,
    context TEXT,
    populations TEXT,
    titles TEXT,
    principles TEXT
);