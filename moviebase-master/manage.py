from flask_script import Manager
from moviebase import app, db, Actor, Movie

manager = Manager(app)


# reset the database and create some initial data
@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    ryanreynolds = Actor(name='Ryan Reynolds', about='Coldplay is a British rock band.')
    channingtatum = Actor(name='Channing Tatum', about='Maroon 5 is an American pop rock band.')
    movie1 = Movie(name='21 Jump Street', year=2000, actor=channingtatum)
    movie2 = Movie(name='Deadpool', year=2014, actor=ryanreynolds)
    db.session.add(coldplay)
    db.session.add(maroon5)
    db.session.add(movie1)
    db.session.add(movie2)
    db.session.commit()


if __name__ == "__main__":
    manager.run()
