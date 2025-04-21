CREATE TABLE law (
    id TEXT NOT NULL PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    supertype TEXT,
    subtype TEXT,
    image_url TEXT,
    world TEXT NOT NULL,
    decree TEXT,
    date INTEGER,
    purpose TEXT,
    author TEXT,
    jurisdictions TEXT,
    prohibitions TEXT,
    penalties TEXT,
    adjudicators TEXT,
    enforcers TEXT
);