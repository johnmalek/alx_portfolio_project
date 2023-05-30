# Importing classes from the libraries
from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from forms import AddMovieForm, RateMovieForm
from dotenv import load_dotenv
import os
import requests

load_dotenv()

# App and database configuration
app = Flask(__name__)
app.app_context().push()
SECRET_KEY = os.urandom(32)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']
Bootstrap(app)
db = SQLAlchemy(app)

# APIs
MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"
MOVIE_DB_API_KEY = os.environ["MOVIE_DB_API_KEY"]


# Creating the Database
class Movie(db.Model):
    __tablename__ = "movies"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(300), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    img_url = db.Column(db.String(250), nullable=False)


db.create_all()

#Routes
# /
@app.route("/")
def home():
    """ Query the database and return all the movies currently on it
    """
    all_movies = Movie.query.all()
    return render_template("index.html", movies=all_movies)


# /add
@app.route("/add", methods=["GET", "POST"])
def add_movie():
    """handle the route add that is used to add a new movie
    """
    form = AddMovieForm()
    if form.validate_on_submit():
        # Get the title of a movie from the form and pass it as part of the parameters for the api call
        movie_title = form.title.data
        response = requests.get(MOVIE_DB_SEARCH_URL, params={"api_key": MOVIE_DB_API_KEY, "query": movie_title})
        data = response.json()["results"]
        return render_template("select.html", options=data)
    return render_template("add.html", form=form)


# /find
@app.route("/find")
def find_movie():
    """handle the route find used to find a new movie
    """
    # To find a movie, get its Id
    # Pass the id to the movie info url and get more information such as the release date, poster image and overview
    # Store this information in the database
    movie_api_id = request.args.get("id")
    if movie_api_id:
        movie_api_url = f"{MOVIE_DB_INFO_URL}/{movie_api_id}"
        response = requests.get(movie_api_url, params={"api_key": MOVIE_DB_API_KEY, "language": "en-US"})
        data = response.json()
        new_movie = Movie(
            title=data["title"],
            year=data["release_date"].split("-")[0],
            img_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
            description=data["overview"]
        )

        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("home"))


#/edit
@app.route("/edit", methods=["GET", "POST"])
def rate_movie():
    """handle the edit route to edit the rating of a movie
    """
    # To edit the rating of a movie, get its id
    # Query the database for the specific movie
    # Set its rating and send that back to the database
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=form)


# /delete
@app.route("/delete", methods=["GET", "POST"])
def delete_movie():
    """handle the route delete to remove a movie from the collection
    """
    # To delete a movie, get the specific
    # Query the database for the movie and then delete
    # Commit the changes back to the database
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
