import clipboard

#take the contents of clipboard into text
copied = clipboard.paste()
#get rid of excess white space to make transfering to list easier
copied.lstrip()
#toList = list(copied.split(" "))

clipboard.copy(copied)

#print(copied)