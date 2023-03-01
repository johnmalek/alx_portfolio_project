ALX Portfolio Project. 
I created a movie database that enables one to keepa a list of their favorite movies.
It comes in handy for people who lead a busy life and are unable to keep up with their best movies.

Functionality

It works by use of an API. When one wants to add a new movie,
they simply just type in the movie title and the rest is handled by flask restful which makes
the API call to https://www.themoviedb.org/ and returns a list of movies with that title. The 
movie is then added to the database (flask_sqlalchemy) and retrieved and display for the user.