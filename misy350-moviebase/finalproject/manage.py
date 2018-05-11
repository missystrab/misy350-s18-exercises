from flask_script import Manager
from moviebase import app, db, Actor, Movie

manager = Manager(app)

# INITIALIZE DATABASE TABLES
@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    ryanreynolds = Actor(name='Ryan Reynolds', about='Ryan Rodney Reynolds is a Canadian actor, film producer, and screenwriter')
    channingtatum = Actor(name='Channing Tatum', about='Channing Matthew Tatum is an American actor')
    tomcruise= Actor(name="Tom Cruise", about='Thomas Cruise is an American actor and producer')
    movie1 = Movie(name='21 Jump Street', year=2012, actor_id=2)
    movie2 = Movie(name='Deadpool', year=2014, actor_id=1)
    movie3 = Movie(name="Top Gun", year=1986, actor_id=3)
    db.session.add(ryanreynolds)
    db.session.add(channingtatum)
    db.session.add(tomcruise)
    db.session.add(movie1)
    db.session.add(movie2)
    db.session.add(movie3)
    db.session.commit()


if __name__ == "__main__":
    manager.run()
