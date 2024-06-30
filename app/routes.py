from flask import flash, redirect, render_template, url_for

from app import app


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html', title='Colleen & Tim')
