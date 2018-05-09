import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

# setup SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
db = SQLAlchemy(app)

# define database tables
#  initialize the database and insert at least three rows in each table as initial testing data.
class Actors(db.Model):
    __tablename__ = 'actors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    about = db.Column(db.Text)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/show')
def show():
    return render_template('show.html')

@app.route('/update')
def update():
    return render_template('update.html')

@app.route('/delete')
def delete():
    return render_template('delete.html')

if __name__ == '__main__':
    app.run()
