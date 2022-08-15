from flask import (Flask, redirect, request, render_template, flash, abort, url_for)

from .utils import get_original_url_fragment, get_redirect_url_for_fragment, url_is_valid
from . import db
import os

app = Flask(__name__)
app.config['DATABASE_PATH'] = os.path.join(app.root_path, 'url.db')
app.config['SECRET_KEY'] = os.urandom(12).hex()

with app.app_context():
    db.init_db()

@app.teardown_appcontext
def teardown_db(exception):
   db.close_db() 

@app.route('/', methods = ('GET', 'POST'))
def index():
    if request.method == 'POST':
        original_url = request.form['url']
        if not url_is_valid(original_url):
            flash('URL is not valid')
            return redirect(url_for('index'))
        existing_fragment = db.get_fragment(original_url)
        if existing_fragment is None:
            fragment = get_original_url_fragment(original_url)
            db.insert_short_url(original_url, fragment) 
            flash(get_redirect_url_for_fragment(fragment))
        else:
            flash(get_redirect_url_for_fragment(existing_fragment))
        return redirect(url_for('index'))
    return render_template('index.html')

@app.route('/<fragment>')
def fragment_redirect(fragment):
    original_url = db.get_original_url(fragment)
    if original_url is None:
        abort(404)
    return redirect(original_url)

