from flask import (Flask, redirect, request, render_template, flash, abort, url_for)
from os.path import join, exists
import db

app = Flask(__name__)

app.config['DATABASE'] = join(app.root_path, 'urls.db')
app.config['SECRET_KEY'] = 'dev'

if not(exists(app.config['DATABASE'])):
    db.init_db(join(app.root_path, 'schema.sql'))

app.teardown_appcontext(db.close_db)

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
            result = 'URL was created: ' + shortened
        else:
            result = 'This URL is already created: ' + fetched[0]
        flash(result)
        return redirect(url_for('home_page'))

    return render_template('home.html')

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

if __name__ == '__main__':
    app.run(debug=True)