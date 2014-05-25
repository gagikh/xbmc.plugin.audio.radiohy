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

from xbmcswift import Plugin, download_page
from xbmcswift.ext.playlist import playlist
from BeautifulSoup import BeautifulSoup as BS, SoupStrainer as SS

import os
import sys

try:
    import json
except ImportError:
    import simplejson as json
from xbmcswift import xbmc, xbmcgui

__plugin__ = 'RadioHY'
__plugin_id__ = 'plugin.audio.radiohy'

plugin = Plugin(__plugin__, __plugin_id__, __file__)

plugin.register_module(playlist, url_prefix='/_playlist')


def get_streams():
    resp = [
            {
                "Name":"Ar Radio Intercontinental",
                "URLStream":"http://199.195.194.92:8029/",
                "Icon":"http://www.arradio.am/images/m_01.gif"
            },
            {
                "Name":"Armenian Patriotic Radio",
                "URLStream":"http://5.35.246.210:8001/stream",
                "Icon":"http://www.imarmenian.com/association2/wp-content/uploads/2011/12/ARF-Logo-Red.png"
            },
            {
                "Name":"Armenian Pulse Radio",
                "URLStream":"http://50.7.96.210:8134/",
                "Icon":"http://www.armenianpulse.com/wp-content/themes/eGamer/images/radiopage/pulse_radio.jpg"
            },
            {
                "Name":"Lav Radio(FM-107)",
                "URLStream":"http://streams4.museter.com:8218/",
                "Icon":"http://www.fm107.am/images/logo.jpg"
            },
            {
                "Name":"Radio Armenie",
                "URLStream":"http://radioarmenie.relay-network.com:8032/",
                "Icon":"http://www.radioarmenie.com/templates/theme475/images/logo.gif"
            },
            {
                "Name":"Radio AVOL",
                "URLStream":"http://64.150.176.192:8250/stream",
                "Icon":"http://radioavol.org/uploads/donates/donate1x1.png"
            },
            {
                "Name":"Radio AYP",
                "URLStream":"http://stric6.streamakaci.com/radioayp.mp3",
                "Icon":"http://radio-aypfm.com/images/bientot_en_direct.jpg"
            },
            {
                "Name":"Radio Jan",
                "URLStream":"http://streams4.museter.com:8216/",
                "Icon":"http://www.arm-radio.com/wp-content/uploads/2014/02/radio-jan-logo.png"
            },
            {
                "Name":"Radio YAN ARMENIAN",
                "URLStream":"http://5.35.246.210:8000/stream",
                "Icon":"http://www.imarmenian.com/association2/wp-content/uploads/2011/11/radioyan-300x97.jpg"
            },
            {
                "Name":"Radio YAN FOLK",
                "URLStream":"http://5.35.246.210:8002/stream",
                "Icon":"http://old.hooys.com/banasdeghzootyoon/55_P20_Dare_Zadooroghli_a.jpg"
            },
            {
                "Name":"Yerevan Nights",
                "URLStream":"mms://radio.yerevannights.com/YerevanNights",
                "Icon":"http://t2.gstatic.com/images?q=tbn:ANd9GcT_gI2q43Rgxs0Exa6JcZr9X3usmX5fGs2Do6_JDDmSrJ2sva3o"
            }
    ]
    return resp

#### Plugin Views ####

# Default View
@plugin.route('/', default=True)
def show_homepage():
    Streams = get_streams()
    items = []
    for Station in Streams:
        items.append({'label': Station['Name'], 'url': plugin.url_for('startplay', URLStream=Station['URLStream'], Name=Station['Name'], Icon=Station['Icon']), 'thumbnail':Station['Icon']})
    items    
    return plugin.add_items(items)

@plugin.route('/live/<Name>/<URLStream>/<Icon>')
def startplay(URLStream, Name, Icon):
    rtmpurl = URLStream
    Thumb = Icon
    li = xbmcgui.ListItem(Name, Name, Thumb, Thumb)
    li.setInfo('music', {'Title':Name})
    xbmc.Player(xbmc.PLAYER_CORE_MPLAYER).play(rtmpurl, li)
    # Return an empty list so we can test with plugin.crawl() and plugin.interactive()
    return []

if __name__ == '__main__': 
    plugin.run()
