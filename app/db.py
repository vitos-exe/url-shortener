import sqlite3
import os
from flask import g, current_app

from .utils import extract_first_element

FIND_ORIGINAL_URL_BY_FRAGMENT_QUERY = 'SELECT original_url FROM shortened_url WHERE fragment = ?' 
INSERT_QUERY = 'INSERT INTO shortened_url VALUES (?, ?)'
FIND_FRAGMENT_BY_ORIGINAL_URL_QUERY = 'SELECT fragment FROM shortened_url WHERE original_url = ?'

def init_db():
    database_path = current_app.config['DATABASE_PATH']
    if os.path.exists(database_path):
        return

    with open(database_path, 'w'):
        pass

    with current_app.open_resource('schema.sql', 'r') as schema:
        connection = get_db()
        connection.executescript(schema.read())
        connection.commit()

def get_db():
    if 'db' not in g:
        g.db = sqlite3.Connection(current_app.config['DATABASE_PATH'])
    return g.db

def close_db():
    db = g.pop('db', None)
    if db is not None:
        db.close()
        
@extract_first_element
def get_original_url(fragment):
    db = get_db()
    original_url = db.execute(FIND_ORIGINAL_URL_BY_FRAGMENT_QUERY, (fragment,)).fetchone()
    return original_url

def insert_short_url(original_url, fragment):
    db = get_db()
    db.execute(INSERT_QUERY, (fragment, original_url))
    db.commit()

@extract_first_element
def get_fragment(original_url):
    db = get_db()
    short_url = db.execute(FIND_FRAGMENT_BY_ORIGINAL_URL_QUERY, (original_url,)).fetchone()
    return short_url

