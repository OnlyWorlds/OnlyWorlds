CREATE TABLE collective (
    id TEXT NOT NULL PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    supertype TEXT,
    subtype TEXT,
    image_url TEXT,
    world TEXT NOT NULL,
    composition TEXT,
    count INTEGER,
    formation_date INTEGER,
    operator TEXT,
    equipment TEXT,
    activity TEXT,
    temperance TEXT,
    skills TEXT,
    rituals TEXT,
    species TEXT,
    characters TEXT,
    creatures TEXT,
    phenomena TEXT
);