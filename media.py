class Movie():
    '''
    A base class for movie objects
    Movies will contain:
    title: the movie title
    poster_image_url: url to the poster image
    trailer_youtube_url: url to the youtube video trailer
    '''
    def __init__(self, title, poster_url, youtube_url):
        self.title=title
        self.poster_image_url=poster_url
        self.trailer_youtube_url = youtube_url

    def print_movie_info(self):
        """Log function to check movie data """
        print("Title:"+self.title)
        print("poster_image_url:"+self.poster_image_url)
        print("trailer_youtube_url:"+self.trailer_youtube_url)
