from flask import Flask, render_template, session
from scripts import helpers

app = Flask(__name__)
if 'pack_id' not in session:
    session['pack_id'] = helpers.makePackID()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')