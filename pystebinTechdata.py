import clipboard
import csv
import os
from datetime import datetime

#take the contents of clipboard into text
copied = clipboard.paste()
#get rid of excess white space to make transfering to list easier
toList = list(copied.split("\n"))
#create 2d array to be edited to go into CSV file
toClip = []
for lines in toList:
    temp = list(lines.split("\t"))
    toClip.append(temp)
#clean up list to needed elements
for lines in toClip:
    del lines[0:2]
    del lines[1:-1]
    del lines [-1]

clip = ""
for lines in toClip:
    clip += lines[0] + '\n'

clipboard.copy(clip)