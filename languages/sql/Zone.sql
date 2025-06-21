CREATE TABLE zone (
    id TEXT NOT NULL PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    supertype TEXT,
    subtype TEXT,
    image_url TEXT,
    world TEXT NOT NULL,
    function TEXT,
    start_date INTEGER,
    end_date INTEGER,
    phenomena TEXT,
    history TEXT,
    claimed_by TEXT,
    roamed_by TEXT,
    titles TEXT
);