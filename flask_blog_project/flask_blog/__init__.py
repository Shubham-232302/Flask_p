from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '0a0e56d1dba88a11623a53a2dc0472db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.app_context().push()

db = SQLAlchemy(app)

from flask_blog import routes