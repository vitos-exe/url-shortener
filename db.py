import sqlite3
from flask import g, current_app
from string import ascii_letters
from random import choice

def init_db(schema):
    with open(schema) as s:
        db = sqlite3.connect('urls.db')
        db.executescript(s.read())
        db.commit()

def get_db():
    if 'db' not in g:
        g.db = sqlite3.Connection(current_app.config['DATABASE'])
    return g.db

def close_db(e = None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def get_short_url():
    while True:
        new = ''.join([choice(ascii_letters) for _ in range(5)])
        exists = get_db().execute(
            'SELECT * FROM url WHERE short_url = ?',
            (new, )
        ).fetchone()
        if not(exists):
            return new