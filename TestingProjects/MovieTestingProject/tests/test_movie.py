from unittest import TestCase
from movies.movie import Movie


class TestMovie(TestCase):

    def test_new_Movie_has_0_likes(self):
        m = Movie("Star Wars", "Lucas", 1977)
        self.assertEqual(0, m.get_likes(), "Should have 0 likes by default")

    def test_new_movie_with_1_like_has_1_like_in_total(self):
        m = Movie("Star Wars", "Lucas", 1977)
        m.like()
        self.assertEqual(1, m.get_likes(), "Should have 1 like after 1 call to like()")

    def test_new_movie_created_increments_id_by_1(self):
        m1 = Movie("Star Wars", "Lucas", 1977)
        id1 = m1.get_movie_id()
        m2 = Movie("Empire Strikes Back", "Lucas", 1981)
        id2 = m2.get_movie_id()
        self.assertEqual(1, id2 - id1, "Should have id+1")
