from flask import Flask, render_template, url_for

app = Flask(__name__)


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

if __name__ == '__main__':
    app.run(debug=True)
    
    
    #Set-ExecutionPolicy RemoteSigned -Scope CurrentUser