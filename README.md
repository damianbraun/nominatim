nominatim
=========

OSM Nominatim API module

tested with **Python 2.7.6** and **Python 3.4.0**

##Quick Start

```
In [1]: from nominatim import Nominatim, NominatimReverse

In [2]: nom = Nominatim()

In [3]: nom.query('58 Parker Street London')
Out[3]: 
[{u'boundingbox': [u'51.5162200927734',
   u'51.516357421875',
   u'-0.120491504669189',
   u'-0.12029179930687'],
  u'class': u'place',
  u'display_name': u'58, Parker Street, Holborn, St Giles, London Borough of Camden, London, Greater London, England, WC2, United Kingdom',
  u'importance': 0.421,
  u'lat': u'51.5162894',
  u'licence': u'Data \xa9 OpenStreetMap contributors, ODbL 1.0. http://www.openstreetmap.org/copyright',
  u'lon': u'-0.120392595530143',
  u'osm_id': u'148391190',
  u'osm_type': u'way',
  u'place_id': u'83887926',
  u'type': u'house'}]

In [4]: nomrev = NominatimReverse()

In [5]: nomrev.query(lat=51.51640, lon=-0.12036)
Out[5]: 
{u'address': {u'city': u'Greater London',
  u'country': u'United Kingdom',
  u'country_code': u'gb',
  u'house': u'Parker Tower',
  u'house_number': u'43-49',
  u'neighbourhood': u'Holborn',
  u'postcode': u'WC2',
  u'road': u'Parker Street',
  u'state': u'England',
  u'suburb': u'St Giles'},
 u'display_name': u'Parker Tower, 43-49, Parker Street, Holborn, St Giles, London Borough of Camden, London, Greater London, England, WC2, United Kingdom',
 u'lat': u'51.5163998',
 u'licence': u'Data \xa9 OpenStreetMap contributors, ODbL 1.0. http://www.openstreetmap.org/copyright',
 u'lon': u'-0.120774554750572',
 u'osm_id': u'97237923',
 u'osm_type': u'way',
 u'place_id': u'64398568'}
 ```
