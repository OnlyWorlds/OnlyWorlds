CREATE TABLE language (
    id TEXT NOT NULL PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    supertype TEXT,
    subtype TEXT,
    image_url TEXT,
    world TEXT NOT NULL,
    phonology TEXT,
    grammar TEXT,
    lexicon TEXT,
    writing TEXT,
    classification TEXT,
    status TEXT,
    spread TEXT,
    dialects TEXT
);