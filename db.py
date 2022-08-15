import sqlite3
from flask import g, current_app
from string import ascii_letters
from random import choice

#function that initializes new database
def init_db(schema):
    with open(schema) as s:
        db = sqlite3.connect('urls.db')
        db.executescript(s.read())
        db.commit()

#function that opens new database connection and stores it in g object
def get_db():
    if 'db' not in g:
        g.db = sqlite3.Connection(current_app.config['DATABASE'])
    return g.db

#function that closes database connection 
def close_db(e = None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

#function that creates new shortened URL 
def get_short_url():
    while True:
        new = ''.join([choice(ascii_letters) for _ in range(5)])
        exists = get_db().execute(
            'SELECT * FROM url WHERE short_url = ?',
            (new, )
        ).fetchone()
        if not(exists):
            return new