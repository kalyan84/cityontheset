from cityontheset.cityontheset.tests import helpers

__author__ = 'kalyang'

import unittest

OBJECT_ENDPOINT = "movies"
class Test_Movies(unittest.TestCase):
    def test_getById(self):
        query_params = {"id":1}
        data = helpers.invokeURL(OBJECT_ENDPOINT, query_params)
        self.assertEqual(data[0]['id'], 1)

    def test_getByTitle(self):
        query_params = {"name":"dawn of the planet"}
        data = helpers.invokeURL(OBJECT_ENDPOINT, query_params)
        self.assertEqual(len(data), 1)

    def test_getByTitle_Empty(self):
        query_params =  {"name":""}
        data = helpers.invokeURL(OBJECT_ENDPOINT, query_params)
        self.assertEqual(len(data), len(helpers.invokeURL(OBJECT_ENDPOINT,None)))

    def test_getByTitle_NotExist(self):
        query_params =  {"name":"this movie does not exist"}
        data = helpers.invokeURL(OBJECT_ENDPOINT, query_params)
        self.assertEqual(len(data), 0)

    def test_getByTitle_Multiple(self):
        query_params =  {"name":"the"}
        data = helpers.invokeURL(OBJECT_ENDPOINT, query_params)
        self.assertEqual(len(data), 66)

    def test_getByTitle_Multiple_Limit(self):
        query_params =  {"name":"the", "limit":"10"}
        data = helpers.invokeURL(OBJECT_ENDPOINT, query_params)
        self.assertEqual(len(data), 10)

    def test_getByIdAndTitle(self):
        query_params = {"id":1, "name":"jitney"}
        data = helpers.invokeURL(OBJECT_ENDPOINT, query_params)
        self.assertTrue(len(data) == 1 and data[0]['id'] == 1)

    def test_getByTitle_Sort_Desc(self):
        query_params = {"name":"the", "limit":10, "sort":"-release_year"}
        data = helpers.invokeURL(OBJECT_ENDPOINT, query_params)
        prev_release_yr = 9999

        for idx,elem in enumerate(data):
            self.assertTrue(prev_release_yr >= data[idx]['release_year'])
            prev_release_yr = data[idx]['release_year']

    def test_getByTitle_Sort_Asc(self):
        query_params = {"name":"the", "limit":10, "sort":"release_year"}
        data = helpers.invokeURL(OBJECT_ENDPOINT, query_params)
        prev_release_yr = 0

        for idx,elem in enumerate(data):
            self.assertTrue(prev_release_yr <= data[idx]['release_year'])
            prev_release_yr = data[idx]['release_year']

    def test_SqlInjection(self):
        query_params = {"name":"ok;delete from movies where id = 1;"}
        helpers.invokeURL(OBJECT_ENDPOINT, query_params)
        query_params = {"id":"1"}
        data = helpers.invokeURL(OBJECT_ENDPOINT, query_params)
        self.assertEqual(len(data), 1)

