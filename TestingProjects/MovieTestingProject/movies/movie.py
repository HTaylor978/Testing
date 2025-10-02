class Movie:
    next_movie_id = 1

    def __init__(self, title, director, year, likes=0, movie_id=0):
        self._title = title
        self._director = director
        self._year = year
        self._likes = likes
        if not movie_id:
            movie_id = Movie.next_movie_id
            Movie.next_movie_id += 1
        self._movie_id = movie_id

    def get_title(self):
        return self._title

    def get_director(self):
        return self._director

    def get_year(self):
        return self._year

    def get_likes(self):
        return self._likes

    def like(self):
        self._likes += 1

    def get_movie_id(self):
        return self._movie_id

    @classmethod
    def get_next_movie_id(cls):
        return cls.next_movie_id
