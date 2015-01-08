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

streams = stations.getStations(_sort_stations)
emails = []
backup = {}
urls = []
icons = []

for station in streams:
    email = station['Email']
    if email:
        emails.append(email)
    icon = station['Icon']
    if icon:
        icons.append(icon)

    uri = station["Url"]
    verified = station['Verified']
    if 'false' == verified:
        continue

    backup = {}
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

        path["nickname"] = station["Name"]

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

# print
b = json.dumps(backup, sort_keys=True, indent=4)
e = json.dumps(emails, sort_keys=True, indent=4)
i = json.dumps(icons,  sort_keys=True, indent=4)

fb = open('backup.json', 'w')
print >> fb, b.replace('/', '\/')
fb.close()
