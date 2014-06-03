import json
import logging
import urllib2


class Nominatim(object):
    """Class for querying text adress

http://wiki.openstreetmap.org/wiki/Nominatim#Search"""
    def __init__(self):
        self.url = 'http://nominatim.openstreetmap.org/search?format=json'
        self.logger = logging.getLogger(__name__)

    def query(self, query, acceptlanguage='', limit=None):
        """Method takes query string, acceptlanguage string (rfc2616 language 
code), limit integer (limits number of results)."""
        query = query.replace(' ', '+')
        url = self.url
        url += '&q=' + query
        if acceptlanguage:
            url += '&accept-language=' + acceptlanguage
        if limit:
            url += '&limit=' + str(limit)
        self.logger.debug('url:\n' + url)
        response = urllib2.urlopen(url)
        result = json.loads(response.read())
        return result


class NominatimReverse(object):
    """Class for querying gps coordinates

http://wiki.openstreetmap.org/wiki/Nominatim#Reverse_Geocoding_.2F_Address_lookup"""
    def __init__(self):
        self.url = 'http://nominatim.openstreetmap.org/reverse?format=json'
        self.logger = logging.getLogger(__name__)

    def query(self, lat=None, lon=None, acceptlanguage='', zoom=18):
        """Method takes lat and lon for GPS coordinates, acceptlanguage string,
zoom integer (between from 0 to 18). """
        url = self.url
        if lat and lon:
            url += '&lat=' + str(lat) + '&lon=' + str(lon)
        if acceptlanguage:
            url += '&accept-language=' + acceptlanguage
        if zoom < 0 or zoom > 18:
            raise Exception('zoom must be betwen 0 and 18')
        url +='&zoom=' + str(zoom)
        self.logger.debug('url:\n' + url)
        response = urllib2.urlopen(url)
        result = json.loads(response.read())
        return result

