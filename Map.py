"""
  Pulled from Livid's Base script
"""

CHANNEL = 0		#main channel (0 - 15)
BASE_PADS = [[60, 61, 62, 63, 64, 65, 66, 67], 
            [52, 53, 54, 55, 56, 57, 58, 59], 
            [44, 45, 46, 47, 48, 49, 50, 51],
            [36, 37, 38, 39, 40, 41, 42, 43]]
BASE_TOUCHSTRIPS = [1, 2, 3, 4, 5, 6, 7, 8]	
BASE_MASTER = 9
BASE_TOUCHPADS = [10, 11, 12, 13, 14, 15, 16, 17]
BASE_BUTTONS = [18, 19, 20, 21, 22, 23, 24, 25]	
BASE_RUNNERS = [68, 69, 70, 71, 72, 73, 74, 75] # Secondary lights
BASE_LCDS = [34, 35]
FOLLOW = True		#this sets whether or not the last selected device on a track is selected for editing when you select a new track
FADER_FEEDBACK_ON = tuple([191, 122, 72]) 

# What do these do?
STREAMINGON = (240, 0, 1, 97, 12, 62, 127, 247)

