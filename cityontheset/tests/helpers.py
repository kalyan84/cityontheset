from config import config

__author__ = 'kalyang'

import json, urllib2, urllib


def invokeURL(object, query_params):
    url = "http://%s/%s/api/%s/?" % (config['host'], config['appname'], object)
    if query_params:
        url = url + urllib.urlencode(query_params)
    response = urllib2.urlopen(url)
    raw_data = response.read().decode('utf-8')
    data = json.loads(raw_data)
    return data
