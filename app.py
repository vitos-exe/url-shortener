from flask import (Flask, redirect, request, render_template, flash, abort, url_for)
from os.path import join, exists
import db

#creating an app instance and configuring it 
app = Flask(__name__)
app.config['DATABASE'] = join(app.root_path, 'urls.db')
app.config['SECRET_KEY'] = 'dev'

#creates new database if it is missing
if not(exists(app.config['DATABASE'])):
    db.init_db(join(app.root_path, 'schema.sql'))

#adds function that closes database after completing request
app.teardown_appcontext(db.close_db)

#view for homepage, which returns its template as response or creates a shortened new URL(if one for inputed doesn't exist) 
@app.route('/', methods = ('GET', 'POST'))
def home_page():
    if request.method == 'POST':
        url = request.form['url']
        database = db.get_db()
        fetched = database.execute(
            'SELECT * FROM url '
            'WHERE original_url = ?',
            (url,)
        ).fetchone()
        if fetched is None:
            shortened = db.get_short_url()
            database.execute(
                'INSERT INTO url VALUES (?, ?)',
                (shortened, url)
            )
            database.commit()
            result = 'URL was created: ' + url_for('home_page', _external = True) + shortened
        else:
            result = 'This URL is already created: ' + url_for('home_page', _external = True) + fetched[0]
        flash(result)
        return redirect(url_for('home_page'))

    return render_template('home.html')

#view for redirecting user to inputed shortened URL(if exists)
@app.route('/<shortened>')
def redirect_url(shortened):
    database = db.get_db()
    original = database.execute(
        'SELECT original_url FROM url '
        'WHERE short_url = ?;',
        (shortened,)
    ).fetchone()
    if original is None:
        abort(404)
    return redirect(original[0])

