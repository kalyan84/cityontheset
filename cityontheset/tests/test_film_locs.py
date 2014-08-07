from cityontheset.cityontheset.tests import helpers

__author__ = 'kalyang'

import unittest

OBJECT_ENDPOINT = "cityfilmlocs"
class Test_Film_Locs(unittest.TestCase):
    def test_getById(self):
        queryParams = {"id":1}
        data = helpers.invokeURL(OBJECT_ENDPOINT, queryParams)
        self.assertEqual(data[0]['id'], 1)

    def test_getByMovieId(self):
        queryParams = {"movie_id":1}
        data = helpers.invokeURL(OBJECT_ENDPOINT, queryParams)
        self.assertEqual(data[0]['movie_id']['id'], 1)

    def test_getByMovieId_Empty(self):
        queryParams =  {"movie_id":""}
        data = helpers.invokeURL(OBJECT_ENDPOINT, queryParams)
        self.assertEqual(len(data), len(helpers.invokeURL(OBJECT_ENDPOINT,None)))

    def test_getByMovieId_NotExist(self):
        queryParams =  {"movie_id":"-1"}
        data = helpers.invokeURL(OBJECT_ENDPOINT, queryParams)
        self.assertEqual(len(data), 0)

    def test_getByMovieTitle_Multiple(self):
        queryParams =  {"name":"the"}
        data = helpers.invokeURL(OBJECT_ENDPOINT, queryParams)
        # if the limit is not specified, the query is limited to 20 records.
        self.assertEqual(len(data), 20)

    def test_getByMovieTitle_Multiple_Limit(self):
        queryParams =  {"name":"the", "limit":"10"}
        data = helpers.invokeURL(OBJECT_ENDPOINT, queryParams)
        self.assertEqual(len(data), 10)

    def test_getByIdAndMovieTitle(self):
        queryParams = {"id":1, "name":"jitney"}
        data = helpers.invokeURL(OBJECT_ENDPOINT, queryParams)
        self.assertTrue(len(data) == 1 and data[0]['id'] == 1)

    def test_SqlInjection(self):
        queryParams = {"name":"ok;delete from cityfilmlocs where id = 1;"}
        helpers.invokeURL(OBJECT_ENDPOINT, queryParams)
        queryParams = {"id":"1"}
        data = helpers.invokeURL(OBJECT_ENDPOINT, queryParams)
        self.assertEqual(len(data), 1)

