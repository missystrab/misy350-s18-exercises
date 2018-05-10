from flask_script import Manager
from songbase import app, db, Artist

manager = Manager(app)

@manager.command
def deploy():
    db.drop_all()
    db.create_all()

    print "inserting initial data"
    coldplay = Artist(name="coldplay", about="this is coldplay")
    m5 = Artist(name="Maroon 5", about="this is maroon 5")

    db.session.add(coldplay)
    db.session.add(m5)

    db.session.commit()

if __name__ == '__main__':
    manager.run()
