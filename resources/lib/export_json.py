#!/usr/bin/env python

# -*- coding: UTF-8 -*-
# Copyright 2014 Gagik Hakobyan
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import stations
import json
import urllib2, httplib

from urlparse import urlparse

_sort_stations = 'Name'

streams = stations.getStations(_sort_stations)
backup = {}
urls = []

def checkAvailability(protocol, hostname, port, path):

    url = protocol + "://" + hostname + ":" + port + path;
    code = 0
    try:
        code = urllib2.urlopen(url).getcode();
        if 200 == code:
            return 0
        else:
            print " status - Error code = ", (code)
            return 1

    except urllib2.HTTPError, e:
        print " status - ", (e.code)
    except urllib2.URLError, e:
        print " status - ", (e.args)
    except httplib.BadStatusLine, e:
        print " status - ", (e.args)

    return 1 

for station in streams:

    # Verification will be done in XBMC version only
    #verified = station['Verified']
    #if 'false' == verified:
    #    continue

    backup = {}
    uri = station["Url"]

    if uri:
        path = {}
        path['address'] = station['Address']
        path['country'] = station['Country']
        path['director']= station['Director']
        path['email']   = station['Email']
        path['icon']    = station['Icon']
        path['phone']   = station['Phone']
        path['time']    = station['Time']
        path['webpage'] = station['WebPage']
        path["nickname"]= station["Name"]

        print "analysing ", uri
        req = urlparse(uri)

        path["protocol"] = req.scheme
        path["hostname"] = req.hostname
        path["path"]     = req.path

        if req.port is None:
            path["port"] = ""
        else:
            path["port"] = str(req.port)

        if 0 == checkAvailability(path["protocol"], path["hostname"], path["port"], path["path"]):
            urls.append(path)

    uri = {}
    uri["uri"] = urls

    backup["backup"] = uri

# print
b = json.dumps(backup, sort_keys=True, indent=4)

fb = open('backup.json', 'w')
print >> fb, 'var stations = ' + b.replace('/', '\/')
fb.close()
