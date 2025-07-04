CREATE TABLE title (
    id TEXT NOT NULL PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    supertype TEXT,
    subtype TEXT,
    image_url TEXT,
    world TEXT NOT NULL,
    authority TEXT,
    eligibility TEXT,
    grant_date INTEGER,
    revoke_date INTEGER,
    issuer TEXT,
    body TEXT,
    superior_title TEXT,
    holders TEXT,
    symbols TEXT,
    status TEXT,
    history TEXT,
    characters TEXT,
    institutions TEXT,
    families TEXT,
    zones TEXT,
    locations TEXT,
    objects TEXT,
    constructs TEXT,
    laws TEXT,
    collectives TEXT,
    creatures TEXT,
    phenomena TEXT,
    species TEXT,
    languages TEXT
);