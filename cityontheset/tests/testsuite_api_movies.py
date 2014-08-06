from cityontheset.cityontheset.tests import helpers

__author__ = 'kalyang'

import unittest


class TestSuite_API_Movies(unittest.TestCase):
    def test_getById(self):
        queryParams = {"id":1}
        data = helpers.invokeURL("movies", queryParams)
        self.assertEqual(data[0]['id'], 1)

    def test_getByTitle(self):
        queryParams = {"name":"dawn of the planet"}
        data = helpers.invokeURL("movies", queryParams)
        self.assertEqual(len(data), 1)

    def test_getByTitle_Empty(self):
        queryParams =  {"name":""}
        data = helpers.invokeURL("movies", queryParams)
        self.assertEqual(len(data), len(helpers.invokeURL("movies",None)))

    def test_getByTitle_NotExist(self):
        queryParams =  {"name":"this movie does not exist"}
        data = helpers.invokeURL("movies", queryParams)
        self.assertEqual(len(data), 0)

    def test_getByTitle_Multiple(self):
        queryParams =  {"name":"the"}
        data = helpers.invokeURL("movies", queryParams)
        self.assertEqual(len(data), 66)

    def test_getByTitle_Multiple_Limit(self):
        queryParams =  {"name":"the", "limit":"10"}
        data = helpers.invokeURL("movies", queryParams)
        self.assertEqual(len(data), 10)

    def test_getByIdAndTitle(self):
        queryParams = {"id":1, "name":"jitney"}
        data = helpers.invokeURL("movies", queryParams)
        self.assertTrue(len(data) == 1 and data[0]['id'] == 1)

    def test_getByTitle_Sort_Desc(self):
        queryParams = {"name":"the", "limit":10, "sort":"-release_year"}
        data = helpers.invokeURL("movies", queryParams)
        prev_release_yr = 9999

        for idx,elem in enumerate(data):
            self.assertTrue(prev_release_yr >= data[idx]['release_year'])
            prev_release_yr = data[idx]['release_year']

    def test_getByTitle_Sort_Asc(self):
        queryParams = {"name":"the", "limit":10, "sort":"release_year"}
        data = helpers.invokeURL("movies", queryParams)
        prev_release_yr = 0

        for idx,elem in enumerate(data):
            self.assertTrue(prev_release_yr <= data[idx]['release_year'])
            prev_release_yr = data[idx]['release_year']

    def test_SqlInjection(self):
        queryParams = {"name":"ok;delete from movies where id = 1;"}
        helpers.invokeURL("movies", queryParams)
        queryParams = {"id":"1"}
        data = helpers.invokeURL("movies", queryParams)
        self.assertEqual(len(data), 1)

