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

from xbmcswift2 import Plugin

import xbmcplugin

import os
import sys

from xbmcswift2 import xbmc, xbmcgui
import xbmcaddon

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
_auto_start             = _settings.getSetting('auto_start')

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
        Streams = stations.getStations()
        idx = 0
        for Station in Streams:
            Address = Station['Address']
            Country = Station['Country']
            Director= Station['Director']
            Email   = Station['Email']
            Icon    = Station['Icon']
            Name    = Station['Name']
            Phone   = Station['Phone']
            Url     = Station['Url']
            WebPage = Station['WebPage']

            if not Url:
                continue

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

            li.setProperty('Id',        str(idx))

            station_list.append(li)
            idx = idx + 1;

        self.list.addItems( station_list )
        self.focusedID = 0
        self.size = len(Streams)
        self.list.selectItem(self.focusedID)
        self.player = xbmc.Player(xbmc.PLAYER_CORE_AUTO)
        self.start = 0
   
    def closeWindow(self):
        #if 1 == self.start:
        #    self.player.stop()
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

            info  = '\nCountry: ' + Country + \
                    '\nEmail:   ' + Email + \
                    '\nPhone:   ' + Phone + \
                    '\nWebPage: ' + WebPage;
            dialog.ok(Name, info)
    
    def onClick(self, controlID):
        flag = 1
        idx = 0
        if STATION_LIST_ID == controlID:
            selItem = self.list.getSelectedItem()
            idx = selItem.getProperty("Id")
        elif BACK_BUTTON_ID == controlID:
            idx = self.focusedID - 1
        elif NEXT_BUTTON_ID == controlID:
            idx = self.focusedID + 1
        else:
            flag = 0

        if flag:
            idx = self.wrapID(idx)
            item = self.list.getListItem(idx)
            Url = item.getProperty("Url");
            Icon = item.getProperty("Icon");
            self.list.selectItem(idx)
            self.focusedID = idx
            self.playStation(Url, Icon)
    
    def playStation(self, Url, Icon):
        self.list = self.getControl( STATION_LIST_ID )
        logo = self.getControl( STATION_LOGO )
        logo.setImage(Icon)
        self.player.play(Url)
        self.start = 1;

    def wrapID(self, id):
        n = self.size
        if (id < 0):
            return n - 1
        elif (id > n - 1):
            return 0
        else:
            return id

    def onFocus(self, controlID):
        #if (STATION_LIST_ID == controlID):
        #    selItem = self.list.getSelectedItem()
        #    self.focusedID = int(selItem.getProperty("Id"))
        pass

# Default View
@plugin.route('/')
def show_homepage():
    gui = WindowBox('skin.xml', _path, _skin, '720p');
    gui.doModal()

if __name__ == '__main__': 
    plugin.run()
