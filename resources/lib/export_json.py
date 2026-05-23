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
    """Checks the availability of a given URL."""
    if not url:
        # print('  - Empty URL, skipping availability check.')
        return 1

    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Python Browser'})
        with urllib.request.urlopen(req, timeout=5) as response:
            code = response.getcode()
            # Optionally, check content type for streams
            # content_type = response.info().get_content_type()
            # if not content_type.startswith(('audio/', 'video/', 'application/vnd.apple.mpegurl')):
            #     print(f'  - URL {url} returned non-streamable content type: {content_type}')
            #     return 1

        if 200 <= code < 300:
            return 0

        print(f'  - URL {url} returned HTTP status code: {code}')
        return 1
    except urllib.error.HTTPError as exc:
        print('http error while analysing ', url)
        print(' status - ', exc.code)
    except urllib.error.URLError as exc:
        print('url error while analysing ', url)
        print(' status - ', exc.args)
    except http.client.BadStatusLine as exc:
        print('bad status line error while analysing ', url)
        print(' status - ', exc.args)
    except socket.timeout as exc:
        # This is the error you observed in the Kodi log
        print(f'  - Timeout error for URL {url}: {exc.args}')
        print('timeout error while analysing ', url)
        print(' status - ', exc.args)

    return 1


def main():
    streams = stations.getStations('Name')
    urls = []

    for station in streams:
        print(f"Checking station: {station['Name']}")
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

        print(f"  - Checking icon availability for {path['icon']}")
        if check_availability(path['icon']) != 0:
            path['icon'] = ''

        print(f"  - Checking stream availability for {uri}")
        if check_availability(uri) == 0:
            urls.append(path)
            print(f"  - Station '{station['Name']}' is VERIFIED.")
        else:
            print(f"  - Station '{station['Name']}' is NOT VERIFIED.")

    backup = {'backup': {'uri': urls}}
    output = json.dumps(backup, sort_keys=True, indent=4)
    output_path = Path(__file__).resolve().parent / 'verified_stations_backup.json'
    output_path.write_text(output, encoding='utf-8')
    print(f"\nExported {len(urls)} verified stations to {output_path.name}")


if __name__ == '__main__':
    main()
