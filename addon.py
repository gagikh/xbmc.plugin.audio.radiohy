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

import os
import sys
import json
from urllib.parse import urlencode, parse_qsl

import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon
import xbmcvfs

_addon   = xbmcaddon.Addon()
_handle  = int(sys.argv[1])
_url     = sys.argv[0]
_lib     = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources', 'lib')
_fanart  = xbmcvfs.translatePath(_addon.getAddonInfo('fanart'))

sys.path.insert(0, _lib)
import stations as _stations

_FAVORITES_PATH = xbmcvfs.translatePath(
    'special://profile/addon_data/plugin.audio.radiohy/favorites.json'
)


def _plugin_url(**kwargs):
    return _url + '?' + urlencode(kwargs)


def _load_favorites():
    if xbmcvfs.exists(_FAVORITES_PATH):
        with xbmcvfs.File(_FAVORITES_PATH) as f:
            try:
                return set(json.loads(f.read()))
            except Exception:
                return set()
    return set()


def _save_favorites(favs):
    folder = os.path.dirname(_FAVORITES_PATH)
    if not xbmcvfs.exists(folder):
        xbmcvfs.mkdirs(folder)
    with xbmcvfs.File(_FAVORITES_PATH, 'w') as f:
        f.write(json.dumps(list(favs)))


def _station_item(station, favorites):
    name       = station['Name']
    icon       = station.get('Icon', '')
    country    = station.get('Country', '')
    stream_url = station.get('Url', '')

    li = xbmcgui.ListItem(name, country)
    li.setArt({'thumb': icon, 'icon': icon, 'fanart': _fanart})
    li.getMusicInfoTag().setTitle(name)
    li.setProperty('IsPlayable', 'true')

    if name in favorites:
        fav_item = ('Remove from Favorites', f'RunPlugin({_plugin_url(action="remove_fav", name=name)})')
    else:
        fav_item = ('Add to Favorites',      f'RunPlugin({_plugin_url(action="add_fav",    name=name)})')

    info_url = _plugin_url(
        action='info', name=name, country=country,
        email=station.get('Email', ''), phone=station.get('Phone', ''),
        webpage=station.get('WebPage', ''),
    )
    li.addContextMenuItems([fav_item, ('Station info', f'RunPlugin({info_url})')])

    play_url = _plugin_url(action='play', url=stream_url, name=name, icon=icon)
    return (play_url, li, False)


# ── Navigation ────────────────────────────────────────────────────────────────

def main_menu():
    entries = [
        ('Favorites',    'DefaultFavourites.png',     _plugin_url(action='favorites')),
        ('By Country',   'DefaultMusicArtists.png',   _plugin_url(action='by_country')),
        ('All Stations', 'DefaultMusicAlbums.png',    _plugin_url(action='all')),
        ('Search',       'DefaultAddonsSearch.png',   _plugin_url(action='search')),
    ]
    items = []
    for label, icon, url in entries:
        li = xbmcgui.ListItem(label)
        li.setArt({'icon': icon, 'thumb': icon, 'fanart': _fanart})
        items.append((url, li, True))

    xbmcplugin.addDirectoryItems(_handle, items)
    xbmcplugin.endOfDirectory(_handle)


def list_favorites():
    favorites  = _load_favorites()
    sort_key   = _addon.getSetting('sort_stations') or 'Name'
    items      = [
        _station_item(s, favorites)
        for s in _stations.getStations(sort_key)
        if s['Name'] in favorites and s.get('Url')
    ]

    if not items:
        li = xbmcgui.ListItem('No favorites yet — use the context menu to add stations')
        xbmcplugin.addDirectoryItem(_handle, '', li, False)
    else:
        xbmcplugin.setContent(_handle, 'files')
        xbmcplugin.addDirectoryItems(_handle, items)
    xbmcplugin.endOfDirectory(_handle)


def list_by_country():
    sort_key = _addon.getSetting('sort_stations') or 'Name'
    buckets  = {}
    for s in _stations.getStations(sort_key):
        if s.get('Url'):
            buckets.setdefault(s.get('Country') or 'Unknown', []).append(s)

    items = []
    for country in sorted(buckets):
        li = xbmcgui.ListItem(f'{country}  ({len(buckets[country])})')
        li.setArt({'icon': 'DefaultMusicArtists.png', 'fanart': _fanart})
        items.append((_plugin_url(action='country', country=country), li, True))

    xbmcplugin.addDirectoryItems(_handle, items)
    xbmcplugin.endOfDirectory(_handle)


def list_country(params):
    country  = params.get('country', '')
    sort_key = _addon.getSetting('sort_stations') or 'Name'
    favorites = _load_favorites()
    items = [
        _station_item(s, favorites)
        for s in _stations.getStations(sort_key)
        if s.get('Country') == country and s.get('Url')
    ]
    xbmcplugin.setContent(_handle, 'files')
    xbmcplugin.addDirectoryItems(_handle, items)
    xbmcplugin.endOfDirectory(_handle)


def list_all():
    sort_key  = _addon.getSetting('sort_stations') or 'Name'
    favorites = _load_favorites()
    items = [
        _station_item(s, favorites)
        for s in _stations.getStations(sort_key)
        if s.get('Url')
    ]
    xbmcplugin.setContent(_handle, 'files')
    xbmcplugin.addDirectoryItems(_handle, items)
    xbmcplugin.endOfDirectory(_handle)


def search():
    query = xbmcgui.Dialog().input('Search stations')
    if not query:
        xbmcplugin.endOfDirectory(_handle, succeeded=False)
        return

    sort_key  = _addon.getSetting('sort_stations') or 'Name'
    favorites = _load_favorites()
    q = query.lower()
    items = [
        _station_item(s, favorites)
        for s in _stations.getStations(sort_key)
        if s.get('Url') and q in s['Name'].lower()
    ]

    if not items:
        xbmcgui.Dialog().notification('RadioHY', f'No results for "{query}"', time=3000)
        xbmcplugin.endOfDirectory(_handle, succeeded=False)
        return

    xbmcplugin.setContent(_handle, 'files')
    xbmcplugin.addDirectoryItems(_handle, items)
    xbmcplugin.endOfDirectory(_handle)


# ── Favorites actions ─────────────────────────────────────────────────────────

def add_favorite(params):
    name = params.get('name', '')
    favs = _load_favorites()
    favs.add(name)
    _save_favorites(favs)
    xbmcgui.Dialog().notification('RadioHY', f'Added: {name}', time=2000)
    xbmc.executebuiltin('Container.Refresh')


def remove_favorite(params):
    name = params.get('name', '')
    favs = _load_favorites()
    favs.discard(name)
    _save_favorites(favs)
    xbmcgui.Dialog().notification('RadioHY', f'Removed: {name}', time=2000)
    xbmc.executebuiltin('Container.Refresh')


# ── Playback ──────────────────────────────────────────────────────────────────

def play_station(params):
    stream_url = params.get('url', '')
    name       = params.get('name', '')
    icon       = params.get('icon', '')

    xbmc.log(f'[RadioHY] play: {name!r} -> {stream_url!r}', xbmc.LOGDEBUG)

    li = xbmcgui.ListItem(name, path=stream_url)
    li.setArt({'thumb': icon})
    li.setMimeType('audio/mpeg')
    li.setContentLookup(False)

    xbmcplugin.setResolvedUrl(_handle, True, li)


# ── Info dialog ───────────────────────────────────────────────────────────────

def show_info(params):
    name    = params.get('name', '')
    s       = _addon.getLocalizedString
    lines   = []
    if params.get('country'): lines.append(f"{s(31003)}: {params['country']}")
    if params.get('email'):   lines.append(f"{s(31002)}: {params['email']}")
    if params.get('phone'):   lines.append(f"{s(31005)}: {params['phone']}")
    if params.get('webpage'): lines.append(f"{s(31007)}: {params['webpage']}")
    xbmcgui.Dialog().ok(name, '\n'.join(lines) if lines else name)


# ── Dispatch ──────────────────────────────────────────────────────────────────

params = dict(parse_qsl(sys.argv[2][1:]))
action = params.get('action', 'menu')

{
    'menu':       main_menu,
    'favorites':  list_favorites,
    'by_country': list_by_country,
    'country':    lambda: list_country(params),
    'all':        list_all,
    'search':     search,
    'add_fav':    lambda: add_favorite(params),
    'remove_fav': lambda: remove_favorite(params),
    'play':       lambda: play_station(params),
    'info':       lambda: show_info(params),
}.get(action, main_menu)()
