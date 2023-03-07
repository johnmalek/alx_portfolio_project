# Import classes from libraries
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import SubmitField, StringField, PasswordField


# Forms
class AddMovieForm(FlaskForm):
    # Form to add a new movie
    title = StringField(label="Movie Title", validators=[DataRequired()])
    add_movie = SubmitField(label="Add Movie")


class RateMovieForm(FlaskForm):
    # Form to change the rating of a movie
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    submit = SubmitField("Done")

