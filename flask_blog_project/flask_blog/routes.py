from flask import render_template, url_for, flash, redirect
from flask_blog import app
from flask_blog.forms import RegistrationForm, LoginForm
# from flask_blog.models import User, Post




posts = [
    {
    'author': 'Shubham Deodhar',
    'title': 'My First Blog',
    'content': 'This is the content',
    'date_posted':'28-feb-2024'
        },
    {
        'author': 'new user',
    'title': 'new Blog',
    'content': 'This is the new content',
    'date_posted':'28-feb-1900'
    }
]

@app.route("/")
def home():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about_page():
    return render_template("about.html", title="about")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}','success')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@gmail.com' and form.password.data == "12345":
            flash(f'You have been logged in','success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful please check username and password!!', 'danger')
                
    return render_template('login.html', title = 'Login', form=form)
