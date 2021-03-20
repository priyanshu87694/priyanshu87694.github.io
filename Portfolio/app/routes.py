from . import app, db
from flask import render_template, request, flash, redirect, url_for
from .forms import MessageForm
from app.models import Message

@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = MessageForm()
    if form.validate_on_submit():
        message = Message(name=form.name.data, email=form.email.data, text=form.text.data)
        db.session.add(message)
        db.session.commit()
        flash('Your message was sent successfully', category='success')
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'Something went wrong {err_msg}', category='danger')

    return render_template('contact.html', form=form)