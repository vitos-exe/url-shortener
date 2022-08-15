CREATE TABLE url(
    short_url text UNIQUE NOT NULL,
    original_url text UNIQUE NOT NULL
);