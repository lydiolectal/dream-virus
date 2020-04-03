from flask import flash, redirect, render_template, request, url_for

from app import app
from app.forms import EmailForm
from app.models import Dream

@app.route('/')
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/archive')
def archive():
    # get all dreams
    dream_da = Dream(id_=1, email='dreamer@gmail.com', initials='DD', location='Philadelphia',date='3/24',content='idk')
    dream_n = Dream(id_=2, email='dreamer2@gmail.com', initials='NN', location='New York City',date='3/25',content='idk')
    dreams = [dream_da, dream_n]
    return render_template('archive.html', dreams=dreams)

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    return render_template('submit.html')

@app.route('/dream-form', methods=['GET', 'POST'])
def dream_form():
    return render_template('dream-form.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
