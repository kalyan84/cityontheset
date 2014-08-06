from cityontheset.cityontheset.tests import helpers

__author__ = 'kalyang'

import unittest

class TestSuite_API_Dump_Data(unittest.TestCase):
    def test_goodJson(self):
        queryParams = {"id":1}
        data = helpers.invokeURL("movies", queryParams)
        self.assertEqual(data[0]['id'], 1)

    def test_existingTitle(self):
        queryParams = {"id":1}
        data = helpers.invokeURL("movies", queryParams)
        self.assertEqual(data[0]['id'], 1)

    def test_newTitle(self):
        queryParams = {"id":1}
        data = helpers.invokeURL("movies", queryParams)
        self.assertEqual(data[0]['id'], 1)

    def test_noTitle(self):
        queryParams = {"id":1}
        data = helpers.invokeURL("movies", queryParams)
        self.assertEqual(data[0]['id'], 1)

    def test_newLocation(self):
        queryParams = {"id":1}
        data = helpers.invokeURL("movies", queryParams)
        self.assertEqual(data[0]['id'], 1)

    def test_noLocation(self):
        queryParams = {"id":1}
        data = helpers.invokeURL("movies", queryParams)
        self.assertEqual(data[0]['id'], 1)

    def test_withFunFact(self):
        queryParams = {"id":1}
        data = helpers.invokeURL("movies", queryParams)
        self.assertEqual(data[0]['id'], 1)

    def test_withoutFunFact(self):
        queryParams = {"id":1}
        data = helpers.invokeURL("movies", queryParams)
        self.assertEqual(data[0]['id'], 1)

    def test_release_year_invalid_chat(self):
        queryParams = {"id":1}
        data = helpers.invokeURL("movies", queryParams)
        self.assertEqual(data[0]['id'], 1)

    def test_same_row_twice(self):
        queryParams = {"id":1}
        data = helpers.invokeURL("movies", queryParams)
        self.assertEqual(data[0]['id'], 1)

    def test_geocode_good(self):
        queryParams = {"id":1}
        data = helpers.invokeURL("movies", queryParams)
        self.assertEqual(data[0]['id'], 1)

    def test_geocode_parantheses(self):
        queryParams = {"id":1}
        data = helpers.invokeURL("movies", queryParams)
        self.assertEqual(data[0]['id'], 1)

    def test_geocode_bad(self):
        queryParams = {"id":1}
        data = helpers.invokeURL("movies", queryParams)
        self.assertEqual(data[0]['id'], 1)
