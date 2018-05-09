MELISSA "MISSY" STRAB
PROFESSOR WANG
MISY 350
MAY 24, 2018

FINAL PROJECT: MOVIE DATABASE

Description: The database I created is a movie database that holds both actors
and movies.  It always users to add, edit, and delete actors from a table as
well as add, edit, and delete movies from a table.  These features are enabled
through forms and extensions from a base webpage.  Each page shares the same
format and navigation bar on the top of the page.  

Database Design:
-I have created two tables: one for the Actors and one for the Movies
-The columns in the Actors table are: name, about
-The columns in the Movies table are: name, year, actor
-It is a one to many relationship because one actor can be involved with many
movies.  The actor field in the movies table links the two tables together.
-The following are outlines of the two tables I have created:

Actors Table
| Actor's Name   | About the Actor|
| :------------- | :------------- |
| Item One       | Item Two       |

Movies Table
| Movie Name     | Movie Year     | Main Actor     |
| :------------- | :------------- | :------------- |
| Item One       | Item Two       | Item Three     |

How to run application (windows instructions):
-First: Install virtual environment
        $ virtualenv venv
-Second: Activate the virtual environment
        $ venv/scripts/activate
-Third: Install all necessary packages
        $ pip install -r requirements.txt
-Fourth: Initialize the database
        $ python manage.py deploy
-Fifth: Run the development server
        $ python manage.py runserver -d
-Sixth: Load the URL in Google Chrome
-Seventh: You should now be able to view the webpage!

SUBMIT URL OF REPO TO CANVAS FOR GRADING PURPOSES
