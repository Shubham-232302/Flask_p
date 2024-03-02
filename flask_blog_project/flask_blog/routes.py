from flask import render_template, url_for, flash, redirect, request
from flask_blog import app, db, bcrypt
from flask_blog.forms import RegistrationForm, LoginForm
from flask_blog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required



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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email = form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account has been created successfully, ypu can login now','success')
        return redirect(url_for('login'))
    return render_template('register.html', title = 'Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login unsuccessful please check username and password!!', 'danger')
        
        # if form.email.data == 'admin@gmail.com' and form.password.data == "12345":
        #     flash(f'You have been logged in','success')
        #     return redirect(url_for('home'))
        # else:
        #     flash('Login unsuccessful please check username and password!!', 'danger')
                
    return render_template('login.html', title = 'Login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/account')
@login_required
def account():
    return render_template('account.html', title = 'Account')
