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

_sort_stations = 'Name'

Streams = stations.getStations(_sort_stations)
emails = []
backup = {}
urls = []

for Station in Streams:
    emails.append(Station["Email"])
    uri = Station["Url"]
    verified = Station['Verified']
    if 'false' == verified:
        continue

    backup = {}
    if uri:
        path = {}
        path["nickname"] = Station["Name"]

        p = uri.find("://")
        protocol = uri[0:p]
        uri = uri[p+3:]
        path["protocol"] = protocol

        p = uri.find(":");
        hostname = uri[0:p]
        uri = uri[p+1:]
        path["hostname"] = hostname

        p = uri.find("/");
        if -1 == p:
            port = uri
            uri = ""
        else:
            port = uri[0:p]
            uri = uri[p:]
        
        if port.isdigit():
            path["port"] = port
        else:
            path["port"] = ""
            uri = port
            port = ""

        path["path"] = uri

        if port:
            urls.append(path)

    uri = {}
    uri["uri"] = urls

    backup["backup"] = uri

print json.dumps(backup, sort_keys=True, indent=4)
