# [Movie Manager](https://johnmalek.github.io/movie_manager_landing/) 😃

!(https://github.com/johnmalek/alx_portfolio_project/blob/main/static/IMG/Screenshot.png?raw=true)

[Movie Manager](https://johnmalek.github.io/movie_manager_landing/) is a website that is essentially a database for movies.

## How it works
* A user clicks on the link [All Movies](https://johnmalek.github.io/movie_manager_landing/) which will launch the website's home page.
* Then click on the [Add Movie](https://movie-manager.onrender.com/) link that will enable one put in the title of a movie will then be used to send an api call to the [Movie Database](https://api.themoviedb.org/3/search/movie) to look for a movie with that title.
* The api returns a list of movies with that title with their release dates. The user picks the specific one and it is displayed on the home page.
* The user can then click on the edit button on the movie to change its rating based on how much he/she likes it.
* The user can also click on the delete button to delete the movie.

## Inspiration
I worked on this project because of a personal problem I faced when I worked for a few years. I would be really busy every Monday - Friday from morning to evening. When I got home I hardly had time for entertainment. I would go straight to bed. When I had time off or during the weekends, I would decide to watch my favorite shows. Now this was a problem because I could not remember the name of a good movie whose trailer I had seen online or the name of a good recommendation made for me by friends and family.
I wanted to create some database that could help me organise these movies. A great UI would also be great. I stumbled upon the [Movie Database](https://api.themoviedb.org/3/search/movie) and thought really hard how I could use it to my adavantage. Luckily, I had knowledge on the [Flask framework](https://flask.palletsprojects.com/en/2.2.x/). I used it to create the restful apis and [SQLALCHEMY](https://www.sqlalchemy.org/) to create the database.
Now I can just relax and whenever I get a good recommendation for a movie, I can just add here and watch it at a future date when I have the time.

## Contributing
[John Malek](https://github.com/johnmalek)

## Related Projects
* [extreme Movie Manager](http://www.binaryworks.it/extrememoviemanager/)
* [Personal Video Database](http://www.videodb.info/forum_en/)
* [GrieeX](http://www.griee.com/)
* [My Movie Manager](http://mymoviemanager.codeplex.com/)
