from movies.movie import Movie

class MoviePersister:
    #_column_names = ('title', 'director', 'year', 'likes', 'movie_id')

    def __init__(self, handler, props):
        self._handler = handler
        self._props = props

    def save_movies(self, movies):
        list_of_dicts = []
        for movie in movies:
            movie_dict = dict()
            for prop in self._props:
                value_of_prop = getattr(movie, '_'+prop)
                movie_dict[prop] = value_of_prop
            list_of_dicts.append(movie_dict)
        self._handler.save_dict_list(list_of_dicts)

    def load_movies(self):
        movie_list = []
        res = self._handler.load_dictlist()
        for m in res:
            movie = Movie(m['title'],m['director'],m['year'],m['likes'],m['movie_id'])
            movie_list.append(movie)
        return movie_list


