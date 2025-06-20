CREATE TABLE institution (
    id TEXT NOT NULL PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    supertype TEXT,
    subtype TEXT,
    image_url TEXT,
    world TEXT NOT NULL,
    doctrine TEXT,
    founding_date INTEGER,
    parent_institution TEXT,
    zones TEXT,
    objects TEXT,
    creatures TEXT,
    status TEXT,
    allies TEXT,
    adversaries TEXT,
    constructs TEXT
);