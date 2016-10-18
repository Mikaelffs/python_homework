import os
import webbrowser

"""Defining the Song class with three atributes and two methods"""

class Song(object):

	def __init__(self, title = "", artist = "", duration = None):
		self.title = title
		self.artist = artist
		self.duration = duration

	"""This method prints the song duration in a prettier way"""	

	def pretty_duration(self):
		hours = self.duration / 3600
		minutes = (self.duration % 3600) / 60
		seconds = (self.duration % 3600) % 60

		return "%02i hours %02i minutes %02i seconds" % (hours, minutes, seconds)

	"""This method opens a web browser window and searches for the song on youtube"""
	
	def play(self):
		webbrowser.open("https://www.youtube.com/results?search_query=" + self.artist + self.title)

"""Open the file lulu_mix_16.csv in the home folder in read-only mode"""
lulusongs = open(os.path.expanduser('~') + "/lulu_mix_16.csv", "r")

"""Make a list of lists with the title, artist and duration of all songs
if the duration contains non-digit characters it is set to zero, if it is
negative a warning is thrown"""

slist = []

for l in lulusongs:
	[title, artist, duration] = (l.strip("\n").split(","))
	if not duration.isdigit(): print "Non number duration"
	if not duration.isdigit(): duration = "0"
	if int(duration) < 0: raise Exception("Negative duration!")
	slist.append([title, artist, duration])

"""Turn the list of lists into a list of Song objects"""
	
songs = [Song(title = title, artist = artist, duration = int(duration)) for title, artist, duration in slist[1:len(slist)]]




"""Close the file with the list of songs"""
lulusongs.close()