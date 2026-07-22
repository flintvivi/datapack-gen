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
        # make sure we have stuff
        pack_id = session.get('pack_id')
        if not pack_id:
            return helpers.apology('pack_id is missing, try deleting cookies', 400)
        helpers.check("framework")

        # give the user their datapack yayyy
        try:
            helpers.makeDatapack(
                namespace=request.form.get('namespace'),
                dpname=request.form.get('dpname'),
                authors=request.form.get('authors'),
                pack_id=pack_id
            )
        except Exception as error:
            return helpers.apology(f'Failed to create datapack! {error}', 500)
    else:
        pack_id = session.get('pack_id')
        return render_template('framework.html')