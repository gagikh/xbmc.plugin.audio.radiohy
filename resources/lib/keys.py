#https://github.com/xbmc/xbmc/blob/master/xbmc/guilib/Key.h

# Analogue - don't change order
KEY_BUTTON_A                        256
KEY_BUTTON_B                        257
KEY_BUTTON_X                        258
KEY_BUTTON_Y                        259
KEY_BUTTON_BLACK                    260
KEY_BUTTON_WHITE                    261
KEY_BUTTON_LEFT_TRIGGER             262
KEY_BUTTON_RIGHT_TRIGGER            263

KEY_BUTTON_LEFT_THUMB_STICK         264
KEY_BUTTON_RIGHT_THUMB_STICK        265

KEY_BUTTON_RIGHT_THUMB_STICK_UP     266 # right thumb stick directions
KEY_BUTTON_RIGHT_THUMB_STICK_DOWN   267 # for defining different actions per direction
KEY_BUTTON_RIGHT_THUMB_STICK_LEFT   268
KEY_BUTTON_RIGHT_THUMB_STICK_RIGHT  269

# Digital - don't change order
KEY_BUTTON_DPAD_UP                  270
KEY_BUTTON_DPAD_DOWN                271
KEY_BUTTON_DPAD_LEFT                272
KEY_BUTTON_DPAD_RIGHT               273

KEY_BUTTON_START                    274
KEY_BUTTON_BACK                     275

KEY_BUTTON_LEFT_THUMB_BUTTON        276
KEY_BUTTON_RIGHT_THUMB_BUTTON       277

KEY_BUTTON_LEFT_ANALOG_TRIGGER      278
KEY_BUTTON_RIGHT_ANALOG_TRIGGER     279

KEY_BUTTON_LEFT_THUMB_STICK_UP      280 # left thumb stick directions
KEY_BUTTON_LEFT_THUMB_STICK_DOWN    281 # for defining different actions per direction
KEY_BUTTON_LEFT_THUMB_STICK_LEFT    282
KEY_BUTTON_LEFT_THUMB_STICK_RIGHT   283

KEY_VMOUSE          0xEFFF

# 0xF000 -> 0xF200 is reserved for the keyboard; a keyboard press is either
KEY_VKEY            0xF000 # a virtual key/functional key e.g. cursor left
KEY_ASCII           0xF100 # a printable character in the range of TRUE ASCII (from 0 to 127) # FIXME make it clean and pure unicode! remove the need for KEY_ASCII
KEY_UNICODE         0xF200 # another printable character whose range is not included in this KEY code

# 0xE000 -> 0xE0FF is reserved for mouse actions
KEY_MOUSE           0xE000

# 0xD000 -> 0xD0FF is reserved for WM_APPCOMMAND messages
KEY_APPCOMMAND      0xD000

# 0xF000 -> 0xF0FF is reserved for mouse actions
KEY_TOUCH           0xF000

KEY_INVALID         0xFFFF

# actions that we have defined...
ACTION_NONE                    0
ACTION_MOVE_LEFT               1
ACTION_MOVE_RIGHT              2
ACTION_MOVE_UP                 3
ACTION_MOVE_DOWN               4
ACTION_PAGE_UP                 5
ACTION_PAGE_DOWN               6
ACTION_SELECT_ITEM             7
ACTION_HIGHLIGHT_ITEM          8
ACTION_PARENT_DIR              9
ACTION_PREVIOUS_MENU          10
ACTION_SHOW_INFO              11

ACTION_PAUSE                  12
ACTION_STOP                   13
ACTION_NEXT_ITEM              14
ACTION_PREV_ITEM              15
ACTION_FORWARD                16 # Can be used to specify specific action in a window, Playback control is handled in ACTION_PLAYER_*
ACTION_REWIND                 17 # Can be used to specify specific action in a window, Playback control is handled in ACTION_PLAYER_*

ACTION_SHOW_GUI               18 # toggle between GUI and movie or GUI and visualisation.
ACTION_ASPECT_RATIO           19 # toggle quick-access zoom modes. Can b used in videoFullScreen.zml window id=2005
ACTION_STEP_FORWARD           20 # seek +1% in the movie. Can b used in videoFullScreen.xml window id=2005
ACTION_STEP_BACK              21 # seek -1% in the movie. Can b used in videoFullScreen.xml window id=2005
ACTION_BIG_STEP_FORWARD       22 # seek +10% in the movie. Can b used in videoFullScreen.xml window id=2005
ACTION_BIG_STEP_BACK          23 # seek -10% in the movie. Can b used in videoFullScreen.xml window id=2005
ACTION_SHOW_OSD               24 # show/hide OSD. Can b used in videoFullScreen.xml window id=2005
ACTION_SHOW_SUBTITLES         25 # turn subtitles on/off. Can b used in videoFullScreen.xml window id=2005
ACTION_NEXT_SUBTITLE          26 # switch to next subtitle of movie. Can b used in videoFullScreen.xml window id=2005
ACTION_SHOW_CODEC             27 # show information about file. Can b used in videoFullScreen.xml window id=2005 and in slideshow.xml window id=2007
ACTION_NEXT_PICTURE           28 # show next picture of slideshow. Can b used in slideshow.xml window id=2007
ACTION_PREV_PICTURE           29 # show previous picture of slideshow. Can b used in slideshow.xml window id=2007
ACTION_ZOOM_OUT               30 # zoom in picture during slideshow. Can b used in slideshow.xml window id=2007
ACTION_ZOOM_IN                31 # zoom out picture during slideshow. Can b used in slideshow.xml window id=2007
ACTION_TOGGLE_SOURCE_DEST     32 # used to toggle between source view and destination view. Can be used in myfiles.xml window id=3
ACTION_SHOW_PLAYLIST          33 # used to toggle between current view and playlist view. Can b used in all mymusic xml files
ACTION_QUEUE_ITEM             34 # used to queue a item to the playlist. Can b used in all mymusic xml files
ACTION_REMOVE_ITEM            35 # not used anymore
ACTION_SHOW_FULLSCREEN        36 # not used anymore
ACTION_ZOOM_LEVEL_NORMAL      37 # zoom 1x picture during slideshow. Can b used in slideshow.xml window id=2007
ACTION_ZOOM_LEVEL_1           38 # zoom 2x picture during slideshow. Can b used in slideshow.xml window id=2007
ACTION_ZOOM_LEVEL_2           39 # zoom 3x picture during slideshow. Can b used in slideshow.xml window id=2007
ACTION_ZOOM_LEVEL_3           40 # zoom 4x picture during slideshow. Can b used in slideshow.xml window id=2007
ACTION_ZOOM_LEVEL_4           41 # zoom 5x picture during slideshow. Can b used in slideshow.xml window id=2007
ACTION_ZOOM_LEVEL_5           42 # zoom 6x picture during slideshow. Can b used in slideshow.xml window id=2007
ACTION_ZOOM_LEVEL_6           43 # zoom 7x picture during slideshow. Can b used in slideshow.xml window id=2007
ACTION_ZOOM_LEVEL_7           44 # zoom 8x picture during slideshow. Can b used in slideshow.xml window id=2007
ACTION_ZOOM_LEVEL_8           45 # zoom 9x picture during slideshow. Can b used in slideshow.xml window id=2007
ACTION_ZOOM_LEVEL_9           46 # zoom 10x picture during slideshow. Can b used in slideshow.xml window id=2007

ACTION_CALIBRATE_SWAP_ARROWS  47 # select next arrow. Can b used in: settingsScreenCalibration.xml windowid=11
ACTION_CALIBRATE_RESET        48 # reset calibration to defaults. Can b used in: settingsScreenCalibration.xml windowid=11/settingsUICalibration.xml windowid=10
ACTION_ANALOG_MOVE            49 # analog thumbstick move. Can b used in: slideshow.xml window id=2007/settingsScreenCalibration.xml windowid=11/settingsUICalibration.xml windowid=10
ACTION_ROTATE_PICTURE_CW      50 # rotate current picture clockwise during slideshow. Can be used in slideshow.xml window id=2007
ACTION_ROTATE_PICTURE_CCW     51 # rotate current picture counterclockwise during slideshow. Can be used in slideshow.xml window id=2007

ACTION_SUBTITLE_DELAY_MIN     52 # Decrease subtitle/movie Delay.  Can b used in videoFullScreen.xml window id=2005
ACTION_SUBTITLE_DELAY_PLUS    53 # Increase subtitle/movie Delay.  Can b used in videoFullScreen.xml window id=2005
ACTION_AUDIO_DELAY_MIN        54 # Increase avsync delay.  Can b used in videoFullScreen.xml window id=2005
ACTION_AUDIO_DELAY_PLUS       55 # Decrease avsync delay.  Can b used in videoFullScreen.xml window id=2005
ACTION_AUDIO_NEXT_LANGUAGE    56 # Select next language in movie.  Can b used in videoFullScreen.xml window id=2005
ACTION_CHANGE_RESOLUTION      57 # switch 2 next resolution. Can b used during screen calibration settingsScreenCalibration.xml windowid=11

REMOTE_0                    58  # remote keys 0-9. are used by multiple windows
REMOTE_1                    59  # for example in videoFullScreen.xml window id=2005 you can
REMOTE_2                    60  # enter time (mmss) to jump to particular point in the movie
REMOTE_3                    61
REMOTE_4                    62  # with spincontrols you can enter 3digit number to quickly set
REMOTE_5                    63  # spincontrol to desired value
REMOTE_6                    64
REMOTE_7                    65
REMOTE_8                    66
REMOTE_9                    67

ACTION_PLAY                 68  # Unused at the moment
ACTION_OSD_SHOW_LEFT        69  # Move left in OSD. Can b used in videoFullScreen.xml window id=2005
ACTION_OSD_SHOW_RIGHT       70  # Move right in OSD. Can b used in videoFullScreen.xml window id=2005
ACTION_OSD_SHOW_UP          71  # Move up in OSD. Can b used in videoFullScreen.xml window id=2005
ACTION_OSD_SHOW_DOWN        72  # Move down in OSD. Can b used in videoFullScreen.xml window id=2005
ACTION_OSD_SHOW_SELECT      73  # toggle/select option in OSD. Can b used in videoFullScreen.xml window id=2005
ACTION_OSD_SHOW_VALUE_PLUS  74  # increase value of current option in OSD. Can b used in videoFullScreen.xml window id=2005
ACTION_OSD_SHOW_VALUE_MIN   75  # decrease value of current option in OSD. Can b used in videoFullScreen.xml window id=2005
ACTION_SMALL_STEP_BACK      76  # jumps a few seconds back during playback of movie. Can b used in videoFullScreen.xml window id=2005

ACTION_PLAYER_FORWARD        77  # FF in current file played. global action, can be used anywhere
ACTION_PLAYER_REWIND         78  # RW in current file played. global action, can be used anywhere
ACTION_PLAYER_PLAY           79  # Play current song. Unpauses song and sets playspeed to 1x. global action, can be used anywhere

ACTION_DELETE_ITEM          80  # delete current selected item. Can be used in myfiles.xml window id=3 and in myvideoTitle.xml window id=25
ACTION_COPY_ITEM            81  # copy current selected item. Can be used in myfiles.xml window id=3
ACTION_MOVE_ITEM            82  # move current selected item. Can be used in myfiles.xml window id=3
ACTION_SHOW_MPLAYER_OSD     83  # toggles mplayers OSD. Can be used in videofullscreen.xml window id=2005
ACTION_OSD_HIDESUBMENU      84  # removes an OSD sub menu. Can be used in videoOSD.xml window id=2901
ACTION_TAKE_SCREENSHOT      85  # take a screenshot
ACTION_RENAME_ITEM          87  # rename item

ACTION_VOLUME_UP            88
ACTION_VOLUME_DOWN          89
ACTION_MUTE                 91
ACTION_NAV_BACK             92
ACTION_VOLAMP_UP            93
ACTION_VOLAMP_DOWN          94

ACTION_CREATE_EPISODE_BOOKMARK 95 #Creates an episode bookmark on the currently playing video file containing more than one episode
ACTION_CREATE_BOOKMARK         96 #Creates a bookmark of the currently playing video file

ACTION_CHAPTER_OR_BIG_STEP_FORWARD       97 # Goto the next chapter, if not available perform a big step forward
ACTION_CHAPTER_OR_BIG_STEP_BACK          98 # Goto the previous chapter, if not available perform a big step back

ACTION_MOUSE_START            100
ACTION_MOUSE_LEFT_CLICK       100
ACTION_MOUSE_RIGHT_CLICK      101
ACTION_MOUSE_MIDDLE_CLICK     102
ACTION_MOUSE_DOUBLE_CLICK     103
ACTION_MOUSE_WHEEL_UP         104
ACTION_MOUSE_WHEEL_DOWN       105
ACTION_MOUSE_DRAG             106
ACTION_MOUSE_MOVE             107
ACTION_MOUSE_END              109

ACTION_BACKSPACE          110
ACTION_SCROLL_UP          111
ACTION_SCROLL_DOWN        112
ACTION_ANALOG_FORWARD     113
ACTION_ANALOG_REWIND      114

ACTION_MOVE_ITEM_UP       115  # move item up in playlist
ACTION_MOVE_ITEM_DOWN     116  # move item down in playlist
ACTION_CONTEXT_MENU       117  # pops up the context menu


# stuff for virtual keyboard shortcuts
ACTION_SHIFT              118
ACTION_SYMBOLS            119
ACTION_CURSOR_LEFT        120
ACTION_CURSOR_RIGHT       121

ACTION_BUILT_IN_FUNCTION  122

ACTION_SHOW_OSD_TIME      123 # displays current time, can be used in videoFullScreen.xml window id=2005
ACTION_ANALOG_SEEK_FORWARD  124 # seeks forward, and displays the seek bar.
ACTION_ANALOG_SEEK_BACK     125 # seeks backward, and displays the seek bar.

ACTION_VIS_PRESET_SHOW        126
ACTION_VIS_PRESET_LIST        127
ACTION_VIS_PRESET_NEXT        128
ACTION_VIS_PRESET_PREV        129
ACTION_VIS_PRESET_LOCK        130
ACTION_VIS_PRESET_RANDOM      131
ACTION_VIS_RATE_PRESET_PLUS   132
ACTION_VIS_RATE_PRESET_MINUS  133

ACTION_SHOW_VIDEOMENU         134
ACTION_ENTER                  135

ACTION_INCREASE_RATING        136
ACTION_DECREASE_RATING        137

ACTION_NEXT_SCENE             138 # switch to next scene/cutpoint in movie
ACTION_PREV_SCENE             139 # switch to previous scene/cutpoint in movie

ACTION_NEXT_LETTER            140 # jump through a list or container by letter
ACTION_PREV_LETTER            141

ACTION_JUMP_SMS2              142 # jump direct to a particular letter using SMS-style input
ACTION_JUMP_SMS3              143
ACTION_JUMP_SMS4              144
ACTION_JUMP_SMS5              145
ACTION_JUMP_SMS6              146
ACTION_JUMP_SMS7              147
ACTION_JUMP_SMS8              148
ACTION_JUMP_SMS9              149

ACTION_FILTER_CLEAR           150
ACTION_FILTER_SMS2            151
ACTION_FILTER_SMS3            152
ACTION_FILTER_SMS4            153
ACTION_FILTER_SMS5            154
ACTION_FILTER_SMS6            155
ACTION_FILTER_SMS7            156
ACTION_FILTER_SMS8            157
ACTION_FILTER_SMS9            158

ACTION_FIRST_PAGE             159
ACTION_LAST_PAGE              160

ACTION_AUDIO_DELAY            161
ACTION_SUBTITLE_DELAY         162

ACTION_RECORD                 170

ACTION_PASTE                  180
ACTION_NEXT_CONTROL           181
ACTION_PREV_CONTROL           182
ACTION_CHANNEL_SWITCH         183
ACTION_CHANNEL_UP             184
ACTION_CHANNEL_DOWN           185
ACTION_NEXT_CHANNELGROUP      186
ACTION_PREVIOUS_CHANNELGROUP  187
ACTION_PVR_PLAY               188
ACTION_PVR_PLAY_TV            189
ACTION_PVR_PLAY_RADIO         190

ACTION_TOGGLE_FULLSCREEN      199 # switch 2 desktop resolution
ACTION_TOGGLE_WATCHED         200 # Toggle watched status (videos)
ACTION_SCAN_ITEM              201 # scan item
ACTION_TOGGLE_DIGITAL_ANALOG  202 # switch digital <-> analog
ACTION_RELOAD_KEYMAPS         203 # reloads CButtonTranslator's keymaps
ACTION_GUIPROFILE_BEGIN       204 # start the GUIControlProfiler running

ACTION_TELETEXT_RED           215 # Teletext Color buttons to control TopText
ACTION_TELETEXT_GREEN         216 #    "       "      "    "     "       "
ACTION_TELETEXT_YELLOW        217 #    "       "      "    "     "       "
ACTION_TELETEXT_BLUE          218 #    "       "      "    "     "       "

ACTION_INCREASE_PAR           219
ACTION_DECREASE_PAR           220

ACTION_VSHIFT_UP              227 # shift up video image in DVDPlayer
ACTION_VSHIFT_DOWN            228 # shift down video image in DVDPlayer

ACTION_PLAYER_PLAYPAUSE       229 # Play/pause. If playing it pauses, if paused it plays.

ACTION_SUBTITLE_VSHIFT_UP     230 # shift up subtitles in DVDPlayer
ACTION_SUBTITLE_VSHIFT_DOWN   231 # shift down subtitles in DVDPlayer
ACTION_SUBTITLE_ALIGN         232 # toggle vertical alignment of subtitles

ACTION_FILTER                 233

ACTION_SWITCH_PLAYER          234

ACTION_STEREOMODE_NEXT        235
ACTION_STEREOMODE_PREVIOUS    236
ACTION_STEREOMODE_TOGGLE      237 # turns 3d mode on/off
ACTION_STEREOMODE_SELECT      238
ACTION_STEREOMODE_TOMONO      239
ACTION_STEREOMODE_SET         240

ACTION_SETTINGS_RESET         241
ACTION_SETTINGS_LEVEL_CHANGE  242

# touch actions
ACTION_TOUCH_TAP              401
ACTION_TOUCH_TAP_TEN          410
ACTION_TOUCH_LONGPRESS        411
ACTION_TOUCH_LONGPRESS_TEN    420

ACTION_GESTURE_NOTIFY         500
ACTION_GESTURE_BEGIN          501
ACTION_GESTURE_ZOOM           502 #sendaction with point and currentPinchScale (fingers together < 1.0 -> fingers apart > 1.0)
ACTION_GESTURE_ROTATE         503
ACTION_GESTURE_PAN            504

ACTION_GESTURE_SWIPE_LEFT       511
ACTION_GESTURE_SWIPE_LEFT_TEN   520
ACTION_GESTURE_SWIPE_RIGHT      521
ACTION_GESTURE_SWIPE_RIGHT_TEN  530
ACTION_GESTURE_SWIPE_UP         531
ACTION_GESTURE_SWIPE_UP_TEN     540
ACTION_GESTURE_SWIPE_DOWN       541
ACTION_GESTURE_SWIPE_DOWN_TEN   550
# 5xx is reserved for additional gesture actions
ACTION_GESTURE_END            599

# The NOOP action can be specified to disable an input event. This is
# useful in user keyboard.xml etc to disable actions specified in the
# system mappings.
ACTION_NOOP                   999

ICON_TYPE_NONE          101
ICON_TYPE_PROGRAMS      102
ICON_TYPE_MUSIC         103
ICON_TYPE_PICTURES      104
ICON_TYPE_VIDEOS        105
ICON_TYPE_FILES         106
ICON_TYPE_WEATHER       107
ICON_TYPE_SETTINGS      109
