from app import app
from flask import render_template, request

@app.route('/')
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/archive')
def archive():
    return render_template('archive.html')

@app.route('/submit')
def submit():
    return render_template('submit.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404