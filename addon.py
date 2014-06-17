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

import xbmcplugin
import xbmcaddon

import os
import sys

from xbmcswift2 import xbmc, xbmcgui
from xbmcswift2 import Plugin

_settings   = xbmcaddon.Addon()

_id                     = _settings.getAddonInfo('id')
_name                   = _settings.getAddonInfo('name')
_version                = _settings.getAddonInfo('version')
_path                   = xbmc.translatePath(_settings.getAddonInfo('path') ).decode('utf-8')
_lib                    = xbmc.translatePath(os.path.join( _path, 'resources', 'lib' ))

_skin                   = _settings.getSetting('skin')
_format                 = _settings.getSetting('format')
_thumbnail_artwork      = _settings.getSetting('thumbnail_artwork')
_sort_stations          = _settings.getSetting('sort_stations')

_auto_start             = "true" == (_settings.getSetting('auto_start'))
_last_station_id        = int(_settings.getSetting('last_station_id'))
_last_focused_station_id= int(_settings.getSetting('last_focused_station_id'))
_languag_name           = _settings.getSetting('language_name')

sys.path.append (_lib)

import keys
import stations

# <!-- 100 = list group -->
# <!-- 200 = back -->
# <!-- 300 = play -->
# <!-- 400 = next -->
# <!-- 500 = station logo -->

STATION_LIST_ID = 100
BACK_BUTTON_ID  = 200
PLAY_BUTTON_ID  = 300
NEXT_BUTTON_ID  = 400
STATION_LOGO    = 500

plugin = Plugin(_name, _id, __file__)

class WindowBox(xbmcgui.WindowXMLDialog):
    
    def onInit(self):
        self.list = self.getControl( STATION_LIST_ID )

        items = []
        station_list = []
        Streams = stations.getStations(_sort_stations)
        idx = 0

        for Station in Streams:
            Address = Station['Address']
            Country = Station['Country']
            Director= Station['Director']
            Email   = Station['Email']
            Icon    = Station['Icon']
            Name    = Station['Name']
            Phone   = Station['Phone']
            Time    = Station['Time']
            Url     = Station['Url']
            WebPage = Station['WebPage']

            li = xbmcgui.ListItem(str(idx) + ") " + Name, Name)
            li.setInfo('music', {'Title': Name})

            li.setProperty('Address',   Address)
            li.setProperty('Country',   Country)
            li.setProperty('Director',  Director)
            li.setProperty('Email',     Email)
            li.setProperty('Icon',      Icon)
            li.setProperty('Name',      Name)
            li.setProperty('Phone',     Phone)
            li.setProperty('Url',       Url)
            li.setProperty('WebPage',   WebPage)
            li.setProperty('Time',      Time)

            li.setProperty('Id',        str(idx))

            station_list.append(li)
            idx = idx + 1;

        self.list.addItems( station_list )
        self.focusedID = 0
        self.stationsCount = len(Streams)
        self.list.selectItem(self.focusedID)
        self.player = xbmc.Player(xbmc.PLAYER_CORE_AUTO)
        if (_auto_start):
            self.runPlayer(_last_station_id)
        else:
            self.list.selectItem(_last_focused_station_id)
   
    def closeWindow(self):
        self.close()

    def onAction(self, action):

        buttonCode =  action.getButtonCode()
        actionID   =  action.getId()
        
        if (actionID in ( \
            keys.ACTION_PREVIOUS_MENU, \
            keys.ACTION_NAV_BACK, \
            keys.ACTION_PARENT_DIR, \
            keys.KEY_BUTTON_BACK)):
            self.closeWindow()
        elif (actionID == keys.ACTION_SHOW_INFO):
            selItem = self.list.getSelectedItem()
            dialog  = xbmcgui.Dialog()

            Address = selItem.getProperty('Address')
            Country = selItem.getProperty('Country')
            Director= selItem.getProperty('Director')
            Email   = selItem.getProperty('Email')
            Name    = selItem.getProperty('Name')
            Phone   = selItem.getProperty('Phone')
            WebPage = selItem.getProperty('WebPage')
            
            emailStr    = _settings.getLocalizedString(31002)
            countryStr  = _settings.getLocalizedString(31003)
            addressStr  = _settings.getLocalizedString(31004)
            phoneStr    = _settings.getLocalizedString(31005)
            directorrStr= _settings.getLocalizedString(31006)
            webStr      = _settings.getLocalizedString(31007)

            info  = "\n" + countryStr + ": " + Country + \
                    "\n" + emailStr   + ": " + Email + \
                    "\n" + phoneStr   + ": " + Phone + \
                    "\n" + webStr     + ": " + WebPage;
            dialog.ok(Name, info)
        else:
            selItem = self.list.getSelectedItem()
            idx = selItem.getProperty("Id")
            _settings.setSetting('last_focused_station_id', idx)
    
    def onClick(self, controlID):
        flag = 1
        idx = 0
        if STATION_LIST_ID == controlID:
            selItem = self.list.getSelectedItem()
            idx = int(selItem.getProperty("Id"))
        elif BACK_BUTTON_ID == controlID:
            idx = self.focusedID - 1
        elif NEXT_BUTTON_ID == controlID:
            idx = self.focusedID + 1
        else:
            flag = 0

        if flag:
            self.runPlayer(idx)
    
    def runPlayer(self, idx):
        idx = self.wrapID(idx, self.stationsCount)
        item = self.list.getListItem(idx)
        Url = item.getProperty("Url");
        Icon = item.getProperty("Icon");
        self.list.selectItem(idx)
        self.focusedID = idx
        self.playStation(Url, Icon)
        _settings.setSetting('last_station_id', str(idx))
    
    def playStation(self, Url, Icon):
        self.list = self.getControl( STATION_LIST_ID )
        logo = self.getControl( STATION_LOGO )
        logo.setImage(Icon)
        self.player.play(Url)

    def wrapID(self, idx, n):
        resp = 0;
        if (idx < 0):
            resp = n - 1
        elif (idx > n - 1):
            resp = 0
        else:
            resp = idx
        return resp

    def onFocus(self, controlID):
        pass

def parse_argv():
    print >> sys.stderr, sys.argv

    try:
        params = dict( arg.split( "=" ) for arg in sys.argv[ 1 ].split( "&" ) )
    except:
        params = {}
    mode  = params.get( "mode", "run" )
    value = params.get( "value","{[* * * * * *],0}" )
    return (mode, value)

# Default View
@plugin.route('/')
def show_homepage():
    mode, value = parse_argv()

    print >> sys.stderr, mode
    print >> sys.stderr, value
    if ("check_time" == parse_argv()):
        return "True"
    else:
        gui = WindowBox('skin.xml', _path, _skin, '720p');
        gui.doModal()
    return

if __name__ == '__main__': 
    plugin.run()
