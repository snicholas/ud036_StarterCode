# Movie Trailer Website project

The project is based on [ud036_StarterCode](https://github.com/adarsh0806/ud036_StarterCode)

The main scope is to show a list of movies with their posters and trailers.
## Usage
To run the program you need python (tested with version 2.7.13).
On the command prompt or terminal run `python main.py` to generate and launch the webpage.

To add new movies to the list modify main.py adding a new movie object. Movie objects requires 3 parameters:
* Title
* url to pposter image
* url to youtube trailer video

 For instance to add Deadpool to the list, add a new Movie object like:
```
deadpool = media.Movie("Deadpool",
                       "https://upload.wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg",
                       "https://www.youtube.com/watch?v=ONHBaC-pfsk")
```
then add it to the list of movies to pass to the fresh_tomatoes.open_movies_page function who will then generate the html page
```
movie_list.append(deadpool)
fresh_tomatoes.open_movies_page(movie_list)
```
