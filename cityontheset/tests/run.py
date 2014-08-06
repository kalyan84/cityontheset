#!/usr/bin/python
import unittest
import sys
import testsuite_api_movies, testsuite_api_film_locs, testsuite_dump_data

def main():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromModule(testsuite_api_movies))
    suite.addTests(loader.loadTestsFromModule(testsuite_api_film_locs))
    suite.addTests(loader.loadTestsFromModule(testsuite_dump_data))
    return unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    if main().wasSuccessful():
        sys.exit(0)
    sys.exit(1)
