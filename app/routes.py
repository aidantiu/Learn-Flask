from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForms

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Joshuahua'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Not Philippines!'
        },
        {
            'author': {'username': 'Lisan Al Gaib'},
            'body': 'The Dune movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/hello')
def hello():
    flash('Hello World!', 'success')
    return redirect(url_for('index'))

@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForms()

    if form.validate_on_submit():
        flash(f"Login request for the user {form.username.data}, remember_me={form.remember_me.data}")
        return redirect(url_for("index"))

    return render_template('login.html', title='Sign In', form=form)