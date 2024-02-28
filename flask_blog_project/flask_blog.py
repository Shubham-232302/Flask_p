from flask import Flask, render_template, url_for, flash
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '0a0e56d1dba88a11623a53a2dc0472db'

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
        flash(f'Account created for {form.username.data}')
    return render_template('register.html', title = 'Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
    
    
    #Set-ExecutionPolicy RemoteSigned -Scope CurrentUser