import clipboard
import csv
import os
from datetime import datetime

#take the contents of clipboard into text
copied = clipboard.paste()
#get rid of excess white space to make transfering to list easier
toList = list(copied.split("\n"))
#create 2d array to be edited to go into CSV file
toCsv = []
for lines in toList:
    temp = list(lines.split("\t"))
    toCsv.append(temp)
#clean up list to needed elements
for lines in toCsv:
    del lines[0]
    del lines[2]
    del lines[3:-1]
    del lines[-1]
    #swap first 2
    lines[0], lines[1] = lines[1], lines[0]

#create csv for export
csvExport = []
csvExport.append(list(['SKU', 'VPN', 'Quantity']))
for lines in toCsv:
    csvExport.append(lines)

#create path for file writing
now = datetime.now()
outline = now.strftime("%d.%m.%Y-%H:%M:%S")
outline = "Ingram-" + outline + ".csv"
outline = os.path.expanduser("~/Desktop/-Order-Scratch/" + outline)

with open(outline, 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csvExport)