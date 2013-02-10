""" Functions for parsing json dictionaries (http or local file)"""
import tempfile
import urllib2
try:
    import simplejson as json
except ImportError:
    import json


def _decode_list(data):
    r"""convert native json unicode to str"""
    retval = []
    for item in data:
        if isinstance(item, unicode):
            item = item.encode('utf-8')
        elif isinstance(item, list):
            item = _decode_list(item)
        elif isinstance(item, dict):
            item = _decode_dict(item)
        retval.append(item)
    return retval


def _decode_dict(data):
    r"""convert native json unicode to str"""
    retval = {}
    for key, value in data.iteritems():
        if isinstance(key, unicode):
            key = key.encode('utf-8')
        if isinstance(value, unicode):
            value = value.encode('utf-8')
        elif isinstance(value, list):
            value = _decode_list(value)
        elif isinstance(value, dict):
            value = _decode_dict(value)
        retval[key] = value
    return retval


def load_json_over_http(url):
    r"""Load a JSON file over http"""
    req = urllib2.Request(url)
    opener = urllib2.build_opener()
    fp_url = opener.open(req)
    retjson = json.load(fp_url, object_hook=_decode_dict)

    return retjson


def load_json(filename):
    r"""Load a JSON file"""
    with open(filename, "r") as fp_json:
        retjson = json.load(fp_json, object_hook=_decode_dict)

    return retjson


def load_json_over_http_file(url):
    r"""alternate implementation which writes a file"""
    req = urllib2.urlopen(url)
    temp_file = tempfile.NamedTemporaryFile()

    chunksize = 16 * 1024
    while True:
        chunk = req.read(chunksize)
        if not chunk:
            break

        temp_file.write(chunk)

    temp_file.flush()

    retjson = json.load(open(temp_file.name, "r"), object_hook=_decode_dict)
    temp_file.close()

    return retjson
