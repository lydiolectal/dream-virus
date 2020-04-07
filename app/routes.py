from flask import flash, jsonify, redirect, render_template, request, url_for

from app import app
from app.forms import DreamForm 
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

@app.route('/email-redirect')
def email_redirect():
    return render_template('email-redirect.html')

@app.route('/_dream_form', methods=['GET', 'POST'])
def get_dream_form():
    if request.method == 'POST':
        # store dream in db
        return redirect ('/archive')
    dream_form = DreamForm()
    html = render_template('dream-form.html', form=dream_form)
    return jsonify({'html': html})

@app.route('/_test_dream_form', methods=['GET', 'POST'])
def _test_dream_form():
    dream_form = DreamForm()
    return render_template('_test_dream_form.html', form=dream_form)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
