import os

from flask import Flask, render_template, request, session
from scripts import helpers

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'default_secret_key')  # Use a default secret key if not set in environment


@app.before_request
def ensure_pack_id():
    if 'pack_id' not in session:
        session['pack_id'] = helpers.makePackID()

@app.errorhandler(404)
def notfound(e):
    return helpers.apology('not found', 404)

@app.errorhandler(500)
def internalerror(e):
    return helpers.apology('internal server error', 500)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/framework', methods=['GET', 'POST'])
def framework():
    if request.method == 'POST':
        pack_id = session.get('pack_id')
        if not pack_id:
            return # temporary
            # return apology('Pack ID not found in session. Try deleting your cookies', 400) TODO: implement
    else:
        pack_id = session.get('pack_id')
        return render_template('framework.html')