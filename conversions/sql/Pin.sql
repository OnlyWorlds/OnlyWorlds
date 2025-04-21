CREATE TABLE pin (
    id TEXT NOT NULL PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    supertype TEXT,
    subtype TEXT,
    image_url TEXT,
    world TEXT NOT NULL,
    map TEXT NOT NULL,
    element TEXT,
    x INTEGER,
    y INTEGER,
    z INTEGER
);