"""
This file allows the reassignment of the controls from their default arrangement.  The order is from left to right; 
Buttons are Note #'s and Faders/Rotaries are Controller #'s

Pulled from the default Livid Base script so I can see the default
CC assignments and so on
"""

CHANNEL = 0		#main channel (0 - 15)
BASE_PADS = [[60, 61, 62, 63, 64, 65, 66, 67], 
            [52, 53, 54, 55, 56, 57, 58, 59], 
            [44, 45, 46, 47, 48, 49, 50, 51],
            [36, 37, 38, 39, 40, 41, 42, 43]]
BASE_TOUCHSTRIPS = [1, 2, 3, 4, 5, 6, 7, 8]		#there are 9 of these
BASE_MASTER = 9
BASE_TOUCHPADS = [10, 11, 12, 13, 14, 15, 16, 17]
BASE_BUTTONS = [18, 19, 20, 21, 22, 23, 24, 25]		#there are 8 of these
BASE_RUNNERS = [68, 69, 70, 71, 72, 73, 74, 75]
BASE_LCDS = [34, 35]
FOLLOW = True		#this sets whether or not the last selected device on a track is selected for editing when you select a new track
TRACK_BANKING_INCREMENT = 8

"""This variable determines whether or not the script automatically arms an instruments track for recording when it is selected"""
AUTO_ARM_SELECTED = True

"""This variable determines whether the octave shift for the note offset controls work as momentary or toggle"""
OFFSET_SHIFT_IS_MOMENTARY = False

"""You can change the orientation of the Up, Down, Left, and Right buttons (where applicable) by changing the array.  The values correspond to the buttons from top to bottom."""
UDLR = [0, 1, 2, 3]

"""The values in this array determine the choices for what length of clip is created when "Fixed Length" is turned on:
0 = 1 Beat
1 = 2 Beat
2 = 1 Bar
3 = 2 Bars
4 = 4 Bars
5 = 8 Bars
6 = 16 Bars
7 = 32 Bars
"""
LENGTH_VALUES = [2, 3, 4]

"""Setting this flag to True will cause Live's detail view to switch to the appropriate one (i.e. Clip vs. Device) when the mode updates"""
SWITCH_VIEWS_ON_MODE_CHANGE = False

"""The following variables contain color values for different operational mode indicators"""
"""[blackkey, whitekey]"""
KEYCOLORS = [7, 3, 4, 5]
DRUMCOLORS = [4, 6]

CHAN_SELECT = 7

MUTE = 2
SOLO = 3
OFFSET = 6
SHIFT_OFFSET = 13
VERTOFFSET = 7
MIDIMODE = 14
USERMODE = 13
SCALEOFFSET = 5
SPLITMODE = 1
SEQUENCERMODE = 6
DRUMBANK = 7
OVERDUB = 5
RECORD = 6
NEW = 2
LENGTH = 3
SELECTED_NOTE = 6

"""[non-banked, banked]"""
SESSION_NAV = [127, 3]
DEVICE_NAV = 5
BANK_NAV = 4
CHAIN_NAV = 11
DEVICE_LAYER = 12


TRACK_MUTE = 2
TRACK_ARM = 5
TRACK_SOLO = 3
TRACK_STOP = 127

STOP_CLIP = 127
CLIP_TRG_PLAY = 13
CLIP_TRG_REC = 11
CLIP_STOP = 1
CLIP_STARTED = 6
CLIP_RECORDING = 5
ZOOM_STOPPED = 127
ZOOM_PLAYING = 6
ZOOM_SELECTED = 8


"""The scale modes and drumpads use the following note maps"""
NOTES = [24, 25, 26, 27, 28, 29, 30, 31, 16, 17, 18, 19, 20, 21, 22, 23, 8, 9, 10, 11, 12, 13, 14, 15, 0, 1, 2, 3, 4, 5, 6, 7]
#DRUMNOTES = [48, 49, 50, 51, 64, 65, 66, 67, 44, 45, 46, 47, 60, 61, 62, 63, 40, 41, 42, 43, 56, 57, 58, 59, 36, 37, 38, 39, 52, 53, 54, 55]
DRUMNOTES = [12, 13, 14, 15, 28, 29, 30, 31, 8, 9, 10, 11, 24, 25, 26, 27, 4, 5, 6, 7, 20, 21, 22, 23, 0, 1, 2, 3, 16, 17, 18, 19]
SCALENOTES = [36, 38, 40, 41, 43, 45, 47, 48, 24, 26, 28, 29, 31, 33, 35, 36, 12, 14, 16, 17, 19, 21, 23, 24, 0, 2, 4, 5, 7, 9, 11, 12]
WHITEKEYS = [0, 2, 4, 5, 7, 9, 11, 12]

"""Any scale names in this array will automatically use SplitMode when chosen, regardless of the SplitSwitch for the individual MIDI Channel"""
SPLIT_SCALES = []

"""This is the default scale used by Auto when something other than a drumrack is detected for the selected track"""
DEFAULT_AUTO_SCALE = 'Major'

"""This is the default Vertical Offset for any scale other than DrumPad """
DEFAULT_VERTOFFSET = 4

"""This is the default NoteOffset, aka RootNote, used for scales other than DrumPad"""
DEFAULT_OFFSET = 48

"""This is the default NoteOffset, aka RootNote, used for the DrumPad scale;  it is a multiple of 4, so an offset of 4 is actually a RootNote of 16"""
DEFAULT_DRUMOFFSET = 9

"""This is the default Scale used for all MIDI Channels"""
DEFAULT_SCALE = 'Auto'

"""This is the default SplitMode used for all MIDI Channels"""
DEFAULT_SPLIT = False


