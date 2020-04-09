from flask import flash, jsonify, redirect, render_template, request, session, url_for

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
    dream_da = Dream(id_=1, email='dreamer@gmail.com', name='DD', location='Philadelphia',date='3/24',content='idk')
    dream_n = Dream(id_=2, email='dreamer2@gmail.com', name='NN', location='New York City',date='3/25',content='idk')
    dreams = [dream_da, dream_n]
    return render_template('archive.html', dreams=dreams)

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    return render_template('submit.html')

@app.route('/email-redirect')
def email_redirect():
    return render_template('email-redirect.html')

@app.route('/access-denied')
def access_denied():
    return render_template('auth-error.html')

@app.route('/_signin')
def signin():
    session['authorized'] = 'True'
    return 'ok'

@app.route('/dream-form', methods=['GET', 'POST'])
def dream_form():
    dream_form = DreamForm()
    authorized = session.get('authorized')
    print('user is authorized:', authorized)
    if dream_form.validate_on_submit():
        # store dream in db
        # 'sign out' user
        session.pop('authorized', None)
        return redirect ('/archive')
    # validate that user is 'signed in'
    # if authorized:
    return render_template('dream-form.html', form=dream_form)
    # return redirect('/access-denied')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
