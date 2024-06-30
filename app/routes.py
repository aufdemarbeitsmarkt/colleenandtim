from flask import flash, redirect, render_template, url_for

from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Colleen & Tim')