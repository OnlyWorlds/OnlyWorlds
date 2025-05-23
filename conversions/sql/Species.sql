CREATE TABLE species (
    id TEXT NOT NULL PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    supertype TEXT,
    subtype TEXT,
    image_url TEXT,
    world TEXT NOT NULL,
    appearance TEXT,
    life_span INTEGER,
    average_weight INTEGER,
    nourishment TEXT,
    instincts TEXT,
    aggression INTEGER,
    agency TEXT,
    languages TEXT,
    impact TEXT,
    habitat TEXT,
    interaction TEXT,
    consumables TEXT
);