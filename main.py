import media
import fresh_tomatoes

# create an empty list which will contain the movies object to pass to fresh_tomatoes.open_movies_page
movie_list=[]

# create the movies object and append them to the movie:_list
star_wars4= media.Movie("Star Wars IV - A new hope",
                        "https://upload.wikimedia.org/wikipedia/en/8/87/StarWarsMoviePoster1977.jpg",
                        "https://www.youtube.com/watch?v=9gvqpFbRKtQ")
movie_list.append(star_wars4)
toy_story = media.Movie('Toy story',
                        'https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
                        'https://www.youtube.com/watch?v=vwyZH85NQC4')
movie_list.append(toy_story)
avatar = media.Movie('Avatar',
                        'https://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg',
                        'https://www.youtube.com/watch?v=-9ceBgWV8io')
movie_list.append(avatar)
tenacious_d = media.Movie('Tenacious D in The Pick of Destiny',
                          'https://upload.wikimedia.org/wikipedia/en/b/b6/Tenacious_d_in_the_pick_of_destiny_ver3.jpg',
                          'https://www.youtube.com/watch?v=TXxQFMG86HA')

deadpool = media.Movie("Deadpool",
                       "https://upload.wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg",
                       "https://www.youtube.com/watch?v=ONHBaC-pfsk")
movie_list.append(deadpool)

# call fresh_tomatoes.open_movies_page to create and show the web page
fresh_tomatoes.open_movies_page(movie_list)
