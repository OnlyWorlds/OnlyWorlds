CREATE TABLE map (
    id TEXT NOT NULL PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    supertype TEXT,
    subtype TEXT,
    image_url TEXT,
    world TEXT NOT NULL,
    background_color TEXT,
    hierarchy INTEGER,
    width INTEGER,
    height INTEGER,
    map TEXT
);