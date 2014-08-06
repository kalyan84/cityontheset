from cityontheset.cityontheset.tests import config

__author__ = 'kalyang'

import json, urllib2, urllib


def invokeURL(queryParams):
    url = "http://"+ config['host']+"/sffilmlocs/api/?"
    url = url + urllib.urlencode(queryParams)
    response = urllib2.urlopen(url)
    raw_data = response.read().decode('utf-8')
    data = json.loads(raw_data)
    return data
