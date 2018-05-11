MELISSA "MISSY" STRAB

PROFESSOR WANG

MISY 350

MAY 24, 2018

FINAL PROJECT: MOVIE DATABASE

*_Description:_*

The database I created is a movie database that holds both actors
and movies.  It allows users to add, edit, and delete actors from a table as
well as add, edit, and delete movies from a table.  These features are enabled
through forms and extensions from a base webpage.  Each page shares the same
format and navigation bar on the top of the page.  

*_Database Design:_*

I have created two tables: one for the Actors and one for the Movies. The columns in the Actors table are: name, about.  The columns in the Movies table are: name, year, actor.  It is a one to many relationship because one actor can be involved with many
movies.  The actor field in the movies table links the two tables together.

The following are outlines of the two tables I have created:

Actors Table

| Actor's Name   | About the Actor|
| :------------- | :------------- |
| Item One       | Item Two       |

Movies Table

| Movie Name     | Movie Year     | Main Actor     |
| :------------- | :------------- | :------------- |
| Item One       | Item Two       | Item Three     |

How to run application (windows instructions):
1. Install virtual environment
        `$ virtualenv venv`
2. Activate the virtual environment
        `$ venv/scripts/activate`
3. Install all necessary packages
        `$ pip install -r requirements.txt`
4. Initialize the database
        `$ python manage.py deploy`
5. Run the development server
        `$ python manage.py runserver -d`
6. Load the URL in Google Chrome
7. You should now be able to view the webpage!
8. Make sure CSS (the look and feel) is visible by clicking SHIFT-CTRL-R
