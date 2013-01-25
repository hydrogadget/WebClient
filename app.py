import sqlite3

from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)
app.debug = True

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    g.db.close()

@app.route('/')
def show_dashboard():
    entries = []
    return render_template('show_dashboard.html', entries=entries)

@app.route('/mobile')
def show_mobile_remote():
    return render_template('mobile_remote.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')

