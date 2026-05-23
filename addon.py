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

import xbmc
import xbmcgui
import xbmcaddon

_settings               = xbmcaddon.Addon()
_version                = _settings.getAddonInfo('version')
_path                   = os.path.dirname(os.path.abspath(__file__))
_lib                    = os.path.join(_path, 'resources', 'lib')

_skin                   = _settings.getSetting('skin')
_format                 = _settings.getSetting('format')
_thumbnail_artwork      = _settings.getSetting('thumbnail_artwork')
_sort_stations          = _settings.getSetting('sort_stations')

_auto_start             = _settings.getSetting('auto_start') == "true"
_last_station_id        = int(_settings.getSetting('last_station_id'))
_last_focused_station_id= int(_settings.getSetting('last_focused_station_id'))
_language_name          = _settings.getSetting('language_name')

sys.path.append(_lib)
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

class WindowBox(xbmcgui.WindowXMLDialog):

    def onInit(self):
        self.list = self.getControl(STATION_LIST_ID)

        station_list = []
        Streams = stations.getStations(_sort_stations)
        idx = 0

        for Station in Streams:
            if 'false' == Station['Verified']:
                continue

            Name    = Station['Name']
            order   = str(idx).zfill(2)

            li = xbmcgui.ListItem(order + ") " + Name, Name)
            li.getMusicInfoTag().setTitle(Name)

            li.setProperty('Address',   Station['Address'])
            li.setProperty('Country',   Station['Country'])
            li.setProperty('Director',  Station['Director'])
            li.setProperty('Email',     Station['Email'])
            li.setProperty('Icon',      Station['Icon'])
            li.setProperty('Name',      Name)
            li.setProperty('Phone',     Station['Phone'])
            li.setProperty('Url',       Station['Url'])
            li.setProperty('WebPage',   Station['WebPage'])
            li.setProperty('Schedule',  Station['Schedule'])
            li.setProperty('Id',        str(idx))
            li.setProperty('Video',     Station['Video'])

            station_list.append(li)
            idx += 1

        self.list.addItems(station_list)
        self.stationsCount = len(station_list)
        self.focusedID = self.clamp_station_index(_last_station_id)

        self.player = xbmc.Player()

        if self.stationsCount == 0:
            return

        self.list.selectItem(self.focusedID)
        if _auto_start:
            self.runPlayer(self.focusedID)
        else:
            self.list.selectItem(self.clamp_station_index(_last_focused_station_id))

    def close_window(self):
        self.close()

    def onAction(self, action):
        actionID = action.getId()

        if actionID in (keys.ACTION_PREVIOUS_MENU, keys.ACTION_NAV_BACK,
                        keys.ACTION_PARENT_DIR, keys.KEY_BUTTON_BACK):
            self.close_window()
        elif actionID == keys.ACTION_SHOW_INFO:
            selItem = self.list.getSelectedItem()
            dialog  = xbmcgui.Dialog()

            Country = selItem.getProperty('Country')
            Director= selItem.getProperty('Director')
            Email   = selItem.getProperty('Email')
            Name    = selItem.getProperty('Name')
            Phone   = selItem.getProperty('Phone')
            WebPage = selItem.getProperty('WebPage')
            Schedule= selItem.getProperty('Schedule')

            emailStr    = _settings.getLocalizedString(31002)
            countryStr  = _settings.getLocalizedString(31003)
            phoneStr    = _settings.getLocalizedString(31005)
            directorStr = _settings.getLocalizedString(31006)
            webStr      = _settings.getLocalizedString(31007)
            timeStr     = _settings.getLocalizedString(31012)

            info = (
                f"\n{countryStr}: {Country}"
                f"\n{emailStr}: {Email}"
                f"\n{phoneStr}: {Phone}"
                f"\n{directorStr}: {Director}"
                f"\n{webStr}: {WebPage}"
                f"\n{timeStr}: {Schedule}"
            )
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
        if self.stationsCount <= 0:
            return

        idx = self.wrapID(idx, self.stationsCount)
        item = self.list.getListItem(idx)
        value = item.getProperty('Schedule')
        flag = self.check_time(value)

        if flag:
            Url   = item.getProperty("Url")
            Icon  = item.getProperty("Icon")
            Video = item.getProperty("Video")
            Name  = item.getProperty("Name")
            self.list.selectItem(idx)
            self.focusedID = idx
            self.setProperty('PlayingStationId', str(idx))
            self.setProperty('PlayingStationName', Name)
            self.playStation(Url, Icon, "true" == Video)
            _settings.setSetting('last_station_id', str(idx))
        else:
            dialog = xbmcgui.Dialog()
            Name = item.getProperty('Name')
            msg = _settings.getLocalizedString(31013)
            dialog.ok(Name, msg)

    def playStation(self, Url, Icon, isVideo):
        logo = self.getControl(STATION_LOGO)
        logo.setImage(Icon)
        li = xbmcgui.ListItem(path=Url)
        self.player.play(Url, li, isVideo)

    def wrapID(self, idx, n):
        if idx < 0:
            return n - 1
        if idx > n - 1:
            return 0
        return idx

    def clamp_station_index(self, idx):
        if self.stationsCount <= 0:
            return 0
        if idx < 0:
            return 0
        if idx >= self.stationsCount:
            return self.stationsCount - 1
        return idx

    def onFocus(self, controlID):
        pass

    def check_time(self, value):
        # Schedule checks are intentionally disabled.
        return True


def run():
    gui = WindowBox('skin.xml', _path, _skin, '720p')
    gui.doModal()


if __name__ == '__main__':
    run()
