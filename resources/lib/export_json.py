#!/usr/bin/env python3

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

import http.client
import json
import socket
from pathlib import Path
import urllib.error
import urllib.request
from urllib.parse import urlparse

import stations


def check_availability(url):
    if not url:
        return False

    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Python Browser'})
        with urllib.request.urlopen(req, timeout=5) as response:
            code = response.getcode()

        if 200 <= code < 300:
            return True

        print(f'  - URL {url} returned HTTP status code: {code}')
        return False
    except urllib.error.HTTPError as exc:
        # 401 means the server is up but requires auth headers (e.g. Zeno.fm streams) — treat as available
        if exc.code == 401:
            return True
        print(f'  - HTTP error for {url}: {exc.code}')
    except urllib.error.URLError as exc:
        print(f'  - URL error for {url}: {exc.reason}')
    except http.client.BadStatusLine:
        # HTTP/0.9 icecast servers respond without a proper status line — treat as available
        return True
    except socket.timeout:
        print(f'  - Timeout for {url}')

    return False


def main():
    streams = stations.getStations('Name')
    urls = []

    for station in streams:
        uri = station['Url']

        if not uri:
            continue

        req = urlparse(uri)

        path = {
            'address': station['Address'],
            'country': station['Country'],
            'director': station['Director'],
            'email': station['Email'],
            'icon': station['Icon'],
            'phone': station['Phone'],
            'schedule': station['Schedule'],
            'webpage': station['WebPage'],
            'nickname': station['Name'],
            'protocol': req.scheme,
            'hostname': req.hostname,
            'path': req.path,
            'port': '' if req.port is None else str(req.port),
        }

        if not check_availability(path['icon']):
            print(f"Checking station: {station['Name']}")
            print(f"  - Checking icon availability for {path['icon']}")
            path['icon'] = ''

        #print(f"  - Checking stream availability for {uri}")
        if check_availability(uri):
            urls.append(path)
            #print(f"  - Station '{station['Name']}' is VERIFIED.")
        else:
            print(f"Checking station: {station['Name']}")
            print(f"  - Station '{station['Name']}' is NOT VERIFIED.")

    output = json.dumps({'backup': {'uri': urls}}, sort_keys=True, indent=4)
    output_path = Path(__file__).resolve().parent / 'stations.json'
    output_path.write_text(output, encoding='utf-8')
    print(f"\nExported {len(urls)} verified stations to {output_path.name}")


if __name__ == '__main__':
    main()
