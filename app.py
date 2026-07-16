import os
import uuid

from flask import Flask, render_template, session
from scripts import helpers

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')
if not app.secret_key:
    raise RuntimeError('SECRET_KEY environment variable is required')

@app.route('/', methods=['GET'])
def index():
    if 'pack_id' not in session:
        session['pack_id'] = str(uuid.uuid4())
    return render_template('index.html')