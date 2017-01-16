#!/usr/bin/env python

import urllib
import urllib2
url = 'http://www.pythontab.com'
values = {'name' : 'Michael Foord',
    'location' : 'pythontab',
        'language' : 'Python' }
data = urllib.urlencode(values)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
the_page = response.read()
print the_page

