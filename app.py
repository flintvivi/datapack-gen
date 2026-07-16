import os

from flask import Flask, render_template, session
from scripts import helpers

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'default_secret_key')  # Use a default secret key if not set in environment


@app.before_request
def ensure_pack_id():
    if 'pack_id' not in session:
        session['pack_id'] = helpers.makePackID()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')