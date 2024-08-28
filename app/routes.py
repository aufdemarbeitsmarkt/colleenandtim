from flask import flash, redirect, render_template, url_for

from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/registry')
def registry():
    return render_template('registry.html')


@app.route('/info')
def info():
    return render_template('info.html')
