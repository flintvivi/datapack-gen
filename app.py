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
    return render_template('404.html'), 404

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/framework', methods=['GET', 'POST'])
def framework():
    if request.method == 'POST':
        pack_id = session.get('pack_id')
        if not pack_id:
            return render_template('400.html'), 400

        namespace = request.form.get('namespace')
        try:
            helpers.uBasicFolderStruct(pack_id, namespace)
        except RuntimeError as e:
            return str(e), 500

        return render_template('framework.html', pack_id=pack_id, namespace=namespace)