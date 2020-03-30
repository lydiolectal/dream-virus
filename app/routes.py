from app import app
from flask import render_template

@app.route('/')
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/dreams')
def dreams():
    return render_template('dreams.html')

@app.route('/submit')
def submit():
    return render_template('submit.html')
