from flask import flash, redirect, render_template, request

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
    # email not yet sent
    form = EmailForm()
    # if form.validate_on_submit():
    #     # send email
    #     send_email(form.data['email'])
    #     return redirect('/about')
    return render_template('submit.html', form=form)

    # email sent -- check email / re-enter email

    # 'logged in'
    

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
