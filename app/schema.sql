CREATE TABLE shortened_url (
    fragment TEXT PRIMARY KEY,
    original_url TEXT UNIQUE NOT NULL
);

