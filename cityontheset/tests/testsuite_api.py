from cityontheset.cityontheset.tests import helpers

__author__ = 'kalyang'

import unittest


class TestSuite_API(unittest.TestCase):
    def test_getById(self):
        queryParams = {"id":1, "title":"jitney"}
        data = helpers.invokeURL(queryParams)
        self.assertEqual(data[0]['id'], 1)

    def test_getByTitle(self):
        queryParams = {"title":"jitney"}
        data = helpers.invokeURL(queryParams)
        self.assertEqual(len(data), 2)
