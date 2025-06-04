CREATE TABLE language (
    id TEXT NOT NULL PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    supertype TEXT,
    subtype TEXT,
    image_url TEXT,
    world TEXT NOT NULL,
    writing TEXT,
    phonology TEXT,
    grammar TEXT,
    vocabulary TEXT,
    classification TEXT,
    prose TEXT,
    speakers INTEGER,
    dialects TEXT,
    range TEXT
);