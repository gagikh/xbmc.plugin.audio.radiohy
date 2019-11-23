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

from xbmcswift2 import (xbmc, xbmcgui, xbmcplugin, xbmcaddon, Request, Plugin)
import os, sys, datetime

_settings               = xbmcaddon.Addon()
_id                     = _settings.getAddonInfo('id')
_name                   = _settings.getAddonInfo('name')
_version                = _settings.getAddonInfo('version')
_path                   = xbmc.translatePath("special://home/addons/" + _id)
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
import keys, stations

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
            Schedule= Station['Schedule']
            Url     = Station['Url']
            Verified= Station['Verified']
            WebPage = Station['WebPage']
            Video   = Station['Video']

            if 'false' == Verified:
                continue

            order = str(idx).zfill(2)

            li = xbmcgui.ListItem(order + ") " + Name, Name)
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
            li.setProperty('Schedule',  Schedule)
            li.setProperty('Id',        str(idx))
            li.setProperty('Video',     Video)

            station_list.append(li)
            idx = idx + 1;

        self.list.addItems( station_list )
        self.focusedID = _last_station_id
        self.stationsCount = len(Streams)
        self.list.selectItem(self.focusedID)
        #self.player = xbmc.Player(xbmc.PLAYER_CORE_AUTO)
        self.player = xbmc.Player()
        if (_auto_start):
            self.runPlayer(_last_station_id)
        else:
            self.list.selectItem(_last_focused_station_id)
   
    def close_window(self):
        self.close()

    def onAction(self, action):

        buttonCode =  action.getButtonCode()
        actionID   =  action.getId()
        
        if (actionID in ( \
            keys.ACTION_PREVIOUS_MENU, \
            keys.ACTION_NAV_BACK, \
            keys.ACTION_PARENT_DIR, \
            keys.KEY_BUTTON_BACK)):
            self.close_window()
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
            Schedule= selItem.getProperty('Schedule')
            
            emailStr    = _settings.getLocalizedString(31002)
            countryStr  = _settings.getLocalizedString(31003)
            addressStr  = _settings.getLocalizedString(31004)
            phoneStr    = _settings.getLocalizedString(31005)
            directorStr = _settings.getLocalizedString(31006)
            webStr      = _settings.getLocalizedString(31007)
            timeStr     = _settings.getLocalizedString(31012)

            info  = "\n" + countryStr + ": " + Country + \
                    "\n" + emailStr   + ": " + Email + \
                    "\n" + phoneStr   + ": " + Phone + \
                    "\n" + directorStr+ ": " + Director + \
                    "\n" + webStr     + ": " + WebPage + \
                    "\n" + timeStr    + ": " + Schedule;
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
        value = item.getProperty('Schedule')
        flag = self.check_time(value)

        if flag:
            Url = item.getProperty("Url");
            Icon = item.getProperty("Icon");
            self.list.selectItem(idx)
            self.focusedID = idx
            self.playStation(Url, Icon)
            _settings.setSetting('last_station_id', str(idx))
        else:
            dialog = xbmcgui.Dialog()
            Name = item.getProperty('Name')
            msg = _settings.getLocalizedString(31013)
            dialog.ok(Name, msg)
    
    def playStation(self, Url, Icon):
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

    def normalize_time(self, old_value, star, new_value):
        if (old_value == star):
            return new_value
        else:
            return old_value

    def check_range(self, start, end, value):
        return (value >= start) & (value <= end)

    def check_time(self, value):
        return True
        now                 = datetime.datetime.now()

        current_minute      = now.minute
        current_hour        = now.hour
        current_month_day   = now.day
        current_month       = now.month
        current_week_day    = now.weekday() + 1
        current_year        = now.year

        val = eval(value);
        for t in val:
            live_start_time = t[0]
            live_end_time   = t[1]

            live_start_minute    = self.normalize_time(live_start_time[0], -1, 0)
            live_start_hour      = self.normalize_time(live_start_time[1], -1, 0)
            live_start_month_day = self.normalize_time(live_start_time[2], -1, 1)
            live_start_month     = self.normalize_time(live_start_time[3], -1, 1)
            live_start_week_day  = self.normalize_time(live_start_time[4], -1, 1)
            live_start_year      = self.normalize_time(live_start_time[5], -1, 1900)

            live_end_minute      = self.normalize_time(live_end_time[0], -1, 59)
            live_end_hour        = self.normalize_time(live_end_time[1], -1, 23)
            live_end_month_day   = self.normalize_time(live_end_time[2], -1, 31)
            live_end_month       = self.normalize_time(live_end_time[3], -1, 12)
            live_end_week_day    = self.normalize_time(live_end_time[4], -1, 7)
            live_end_year        = self.normalize_time(live_end_time[5], -1, 3000)

            if ( 
                    self.check_range(live_start_minute   , live_end_minute   , current_minute   ) &
                    self.check_range(live_start_hour     , live_end_hour     , current_hour     ) &
                    self.check_range(live_start_month_day, live_end_month_day, current_month_day) &
                    self.check_range(live_start_month    , live_end_month    , current_month    ) &
                    self.check_range(live_start_week_day , live_end_week_day , current_week_day ) &
                    self.check_range(live_start_year     , live_end_year     , current_year     )):
                return True
        return False

# Default View
@plugin.route('/')
def run():
    gui = WindowBox('skin.xml', _path, _skin, '720p');
    gui.doModal()

if __name__ == '__main__': 
    plugin.run()
