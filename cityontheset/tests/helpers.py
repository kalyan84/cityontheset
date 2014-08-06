from config import config

__author__ = 'kalyang'

import json, urllib2, urllib


def invokeURL(object, queryParams):
    url = "http://%s/%s/api/%s/?" % (config['host'], config['appname'], object)

    if queryParams:
        url = url + urllib.urlencode(queryParams)

    response = urllib2.urlopen(url)
    raw_data = response.read().decode('utf-8')
    data = json.loads(raw_data)
    return data
