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

from xbmcswift import Plugin

import os
import sys

from xbmcswift import xbmc, xbmcgui
import xbmcaddon

_settings   = xbmcaddon.Addon()

_id         = _settings.getAddonInfo('id')
_name       = _settings.getAddonInfo('name')
_version    = _settings.getAddonInfo('version')
_path       = xbmc.translatePath( _settings.getAddonInfo('path') ).decode('utf-8')
_lib        = xbmc.translatePath( os.path.join( _path, 'resources', 'lib' ) )

plugin = Plugin(_name, _id, __file__)

def get_streams():
    #{
    #    "Name":"HayFM",
    #    "Url":"http://hayfm.am:8000/",
    #    "Icon":""
    #},
    resp = [
            {
                "Name":     "Ar Radio Intercontinental",
                "Url":      "http://199.195.194.92:8029",
                "Icon":     "http://www.arradio.am/images/m_01.gif",
                "Email":    "aa@arradio.am",
                "Country":  "Armenia",
                "Phone":    "+374-10-55-11-43",
                "WebPage":  "http://www.arradio.am"
            },
            {
                "Name":     "Armenian Patriotic Radio",
                "Url":      "http://5.35.246.210:8001/stream",
                "Icon":     "http://www.imarmenian.com/association2/wp-content/uploads/2011/12/ARF-Logo-Red.png",
                "Email":    "radioyan@imarmenian.com",
                "Country":  "France",
                "Phone":    "+961-3-274-847",
                "WebPage":  "http://radioyan.com/"
            },
            {
                "Name":     "Armenian Pulse Radio",
                "Url":      "http://50.7.96.210:8134/",
                "Icon":     "http://www.armenianpulse.com/wp-content/themes/eGamer/images/radiopage/pulse_radio.jpg",
                "Email":    "content@armenianpulse.com",
                "Country":  "",
                "Phone":    "",
                "WebPage":  "http://www.armenianpulse.com/"
            },
            {
                "Name":     "Lav Radio(FM-107)",
                "Url":      "http://streams4.museter.com:8218/",
                "Icon":     "http://www.fm107.am/images/logo.jpg",
                "Email":    "",
                "Country":  "Armenia",
                "Phone":    "+374-10-36-86-45",
                "WebPage":  "http://www.fm107.am/"
            },
            {
                "Name":     "Nor Radyo",
                "Url":      "http://norradyo.com:8000/live",
                "Icon":     "http://www.ermenikultur.org/wp-content/uploads/2013/10/Nor_Radyo__g_rsel.jpg",
                "Email":    "",
                "Country":  "Turkey",
                "Phone":    "",
                "WebPage":  "http://www.norradyo.com/"
            },
            {
                "Name":     "Radio Armenie",
                "Url":      "http://radioarmenie.relay-network.com:8032/",
                "Icon":     "http://www.radioarmenie.com/templates/theme475/images/logo.gif",
                "Email":    "",
                "Country":  "France",
                "Phone":    "04-78-49-52-74",
                "WebPage":  "http://www.radioarmenie.com/"
            },
            {
                "Name":     "Radio AVOL",
                "Url":      "http://64.150.176.192:8250/stream",
                "Icon":     "http://radioavol.org/uploads/donates/donate1x1.png",
                "Email":    "info@radioavol.org",
                "Country":  "Lebanon",
                "Phone":    "",
                "WebPage":  "http://radioavol.org/"
            },
            {
                "Name":     "Radio AYP",
                "Url":      "http://stric6.streamakaci.com/radioayp.mp3",
                "Icon":     "http://radio-aypfm.com/images/bientot_en_direct.jpg",
                "Email":    "",
                "Country":  "France",
                "Phone":    "01-43-53-19-90",
                "WebPage":  "http://radio-aypfm.com/"
            },
            {
                "Name":     "Radio Hay",
                "Url":      "http://mix.am:8000/rhyerevan",
                "Icon":     "",
                "Email":    "",
                "Country":  "Armenia",
                "Phone":    "",
                "WebPage":  "http://radiohay.am/"
            },
            {
                "Name":     "Radio Jan",
                "Url":      "http://streams4.museter.com:8216/",
                "Icon":     "http://www.arm-radio.com/wp-content/uploads/2014/02/radio-jan-logo.png",
                "Email":    "info@radiojan.am",
                "Country":  "Armenia",
                "Phone":    "+374-96-01-08-55",
                "WebPage":  "http://www.radiojan.am/"
            },
            {
                "Name":     "Radio Sevan",
                "Url":      "http://sevan.bitwize.me:8018/",
                "Icon":     "http://cdn9.staztic.com/app/a/991/991430/radio-sevan-live-1-0-s-156x156.jpg",
                "Email":    "",
                "Country":  "Beirut",
                "Phone":    "+961-1-567161/2/3",
                "WebPage":  "http://www.radiosevan.com/"
            },
            {
                "Name":     "Radio YAN ARMENIAN",
                "Url":      "http://5.35.246.210:8000/stream",
                "Icon":     "http://www.imarmenian.com/association2/wp-content/uploads/2011/11/radioyan-300x97.jpg",
                "Email":    "radioyan@imarmenian.com",
                "Country":  "France",
                "Phone":    "+961-3-274-847",
                "WebPage":  "http://www.radioyan.com/"
            },
            {
                "Name":     "Radio YAN FOLK",
                "Url":      "http://5.35.246.210:8002/stream",
                "Icon":     "http://old.hooys.com/banasdeghzootyoon/55_P20_Dare_Zadooroghli_a.jpg",
                "Email":    "radioyan@imarmenian.com",
                "Country":  "France",
                "Phone":    "+961-3-274-847",
                "WebPage":  "http://www.radioyan.com/"
            },
            {
                "Name":     "Yerevan Nights",
                "Url":      "mms://radio.yerevannights.com/YerevanNights",
                "Icon":     "http://t2.gstatic.com/images?q=tbn:ANd9GcT_gI2q43Rgxs0Exa6JcZr9X3usmX5fGs2Do6_JDDmSrJ2sva3o",
                "Email":    "info@yerevannights.com",
                "Country":  "Armenia",
                "Phone":    "",
                "WebPage":  "http://www.yerevannights.com/"
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
        items.append({
                        'label': Station['Name'],
                        'url': plugin.url_for(
                                'startplay',
                                Url=Station['Url'],
                                Name=Station['Name'],
                                Icon=Station['Icon'],
                                Country=Station['Country']),
                        'thumbnail':Station['Icon']})

    return plugin.add_items(items)

@plugin.route('/live/<Name>/<Url>/<Icon>/<Country>')
def startplay(Url, Name, Icon, Country):
    rtmpurl = Url
    Thumb = Icon
    li = xbmcgui.ListItem(Name, Name, Thumb, Thumb)
    li.setInfo('music', {'Title':Name})
    li.setProperty('Path', Url)
    li.setProperty('Country', Country)
    xbmc.Player(xbmc.PLAYER_CORE_MPLAYER).play(rtmpurl, li)
    return []

if __name__ == '__main__': 
    plugin.run()
