from flask_script import Manager
from songbase import app, db, Artist

manager = Manager(app)

#  initialize the database and insert at least three rows in each table as initial testing data.
@manager.command
def deploy():
    db.drop_all()
    db.create_all()

if __name__ == '__main__':
    manager.run()
