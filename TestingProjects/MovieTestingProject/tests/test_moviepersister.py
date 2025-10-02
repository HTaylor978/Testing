from unittest import TestCase
from unittest.mock import Mock
from moviedata.moviepersister import MoviePersister

class TestMoviePersister(TestCase):
    def test_load_movies_with_1_object(self):
        filehandler_mock = Mock()
        props = ('title', 'director', 'year', 'likes', 'movie_id')

        filehandler_mock.load_dictlist.return_value = [{'title':'T','director':'D','year':2000,'likes':1,'movie_id':1000}]
        persister = MoviePersister(filehandler_mock, props)

        result = persister.load_movies()
        self.assertEqual(1, len(result), "Should return 1 Movie")
        self.assertEqual('T',result[0].get_title(), "Title should be T")
        self.assertEqual('D', result[0].get_director(), "Director should be D")
        self.assertEqual(2000, result[0].get_year(), "Year should be 2000")
        self.assertEqual(1, result[0].get_likes(), "Likes should be 1")
        self.assertEqual(1000, result[0].get_movie_id(), "ID should be 1000")

    def test_load_movies_with_2_objects(self):
        filehandler_mock = Mock()
        props = ('title', 'director', 'year', 'likes', 'movie_id')
        d1 = {'title':'T','director':'D','year':2000,'likes':1,'movie_id':1000}
        d2 = {'title':'T','director':'D','year':2000,'likes':9,'movie_id':1001}

        filehandler_mock.load_dictlist.return_value = [d1,d2]
        persister = MoviePersister(filehandler_mock, props)

        result = persister.load_movies()
        self.assertEqual(2, len(result), "Should return 2 Movies")
