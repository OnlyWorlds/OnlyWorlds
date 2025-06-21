CREATE TABLE phenomenon (
    id TEXT NOT NULL PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    supertype TEXT,
    subtype TEXT,
    image_url TEXT,
    world TEXT NOT NULL,
    expression TEXT,
    effects TEXT,
    duration INTEGER,
    catalysts TEXT,
    empowerments TEXT,
    mythology TEXT,
    system TEXT,
    triggers TEXT,
    wielders TEXT,
    environments TEXT
);