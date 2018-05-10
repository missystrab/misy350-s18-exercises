import os
from flask import Flask, session, render_template, request, flash, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess secure key'

# INITIALIZE SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
db = SQLAlchemy(app)

# DEFINITION OF ACTOR TABLE
class Actor(db.Model):
    __tablename__ = 'actors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    about = db.Column(db.Text)
    # one-to-many relationship
    movies = db.relationship('Movie', backref='actor', cascade="delete")

# DEFINITION OF MOVIE TABLE
class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    year = db.Column(db.Integer)
    actor_id = db.Column(db.Integer, db.ForeignKey('actors.id'))

# HOMEPAGE ROUTE
@app.route('/')
def index():
    return render_template('index.html')

# ACTOR TABLE ROUTE
@app.route('/actors')
def show_all_actors():
    actors = Actor.query.all()
    return render_template('actors-all.html', actors=actors)

# ADD ACTOR FORM ROUTE
@app.route('/actors/add/', methods=['GET', 'POST'])
def add_actors():
    if request.method == 'GET':
        return render_template('actors-add.html')
    if request.method == 'POST':
        name = request.form['name']
        about = request.form['about']
        actor = Actor(name=name, about=about)
        db.session.add(actor)
        db.session.commit()
        return redirect(url_for('show_all_actors'))

# ADD ACTOR BUTTON ROUTE
@app.route('/api/actors/add', methods=['POST'])
def add_ajax_actors():
    name = request.form['name']
    about = request.form['about']
    actor = Actor(name=name, about=about)
    db.session.add(actor)
    db.session.commit()
    flash('Actor Inserted', 'success')
    return jsonify({"id": str(actor.id), "name": actor.name})

# EDIT ACTOR ROUTE
@app.route('/actors/edit/<int:id>', methods=['GET', 'POST'])
def edit_actor(id):
    actor = Actor.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('actors-edit.html', actor=actor)
    if request.method == 'POST':
        actor.name = request.form['name']
        actor.about = request.form['about']
        db.session.commit()
        return redirect(url_for('show_all_actors'))

# DELETE ACTOR ROUTE
@app.route('/actors/delete/<int:id>', methods=['GET', 'POST'])
def delete_actor(id):
    actor = Actor.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('actors-delete.html', actor=actor)
    if request.method == 'POST':
        db.session.delete(actor)
        db.session.commit()
        return redirect(url_for('show_all_actors'))

# DELETE AJAX ROUTE
@app.route('/api/actors/<int:id>', methods=['DELETE'])
def delete_ajax_actor(id):
    actor = Actor.query.get_or_404(id)
    db.session.delete(actor)
    db.session.commit()
    return jsonify({"id": str(actor.id), "name": actor.name})

# MOVIE TABLE ROUTE
@app.route('/movies')
def show_all_movies():
    movies = Movie.query.all()
    return render_template('movie-all.html', movies=movies)

# ADD MOVIE FORM ROUTE
@app.route('/movie/add', methods=['GET', 'POST'])
def add_movies():
    if request.method == 'GET':
        actors = Actor.query.all()
        return render_template('movie-add.html', actors=actors)
    if request.method == 'POST':
        name = request.form['name']
        year = request.form['year']
        actor_name = request.form['actor']
        actor = Actor.query.filter_by(name=actor_name).first()
        movie = Movie(name=name, year=year, actor=actor)
        db.session.add(movie)
        db.session.commit()
        return redirect(url_for('show_all_movies'))

# EDIT MOVIE ROUTE
@app.route('/movie/edit/<int:id>', methods=['GET', 'POST'])
def edit_movie(id):
    movie = Movie.query.filter_by(id=id).first()
    actors = Actor.query.all()
    if request.method == 'GET':
        return render_template('movie-edit.html', movie=movie, actors=actors)
    if request.method == 'POST':
        movie.name = request.form['name']
        movie.year = request.form['year']
        actor_name = request.form['actor']
        actor = Actor.query.filter_by(name=actor_name).first()
        movie.actor = actor
        db.session.commit()
        return redirect(url_for('show_all_movies'))

# DELETE MOVIE ROUTE
@app.route('/movie/delete/<int:id>', methods=['GET', 'POST'])
def delete_movie(id):
    movie = Movie.query.filter_by(id=id).first()
    actors = Actor.query.all()
    if request.method == 'GET':
        return render_template('movie-delete.html', movie=movie, actors=actors)
    if request.method == 'POST':
        db.session.delete(movie)
        db.session.commit()
        return redirect(url_for('show_all_movies'))

# DELETE MOVIE AJAX ROUTE
@app.route('/api/movie/<int:id>', methods=['DELETE'])
def delete_ajax_movie(id):
    movie = Movie.query.get_or_404(id)
    db.session.delete(movie)
    db.session.commit()
    return jsonify({"id": str(movie.id), "name": movie.name})

# ABOUT ME ROUTE
@app.route('/about')
def about():
    return render_template('about.html')

# FORM ROUTE
@app.route('/form-demo', methods=['GET', 'POST'])
def form_demo():
    if request.method == 'GET':
        first_name = request.args.get('first_name')
        if first_name:
            return render_template('form-demo.html', first_name=first_name)
        else:
            return render_template('form-demo.html', first_name=session.get('first_name'))
    if request.method == 'POST':
        session['first_name'] = request.form['first_name']
        return redirect(url_for('form_demo'))

# GET MOVIE ID ROUTE
@app.route('/movie/<int:id>/')
def get_movie_id(id):
    return "Hi, this is %s and the movie's id is %d" % ('administrator', id)

# RUN PROGRAM
if __name__ == '__main__':
    app.run()
