from flask_script import Manager
from songbase import app, db, Artist

manager = Manager(app)

@manager.command
def deploy():
    db.drop_all()
    db.create_all()

if __name__ == '__main__':
    manager.run()
