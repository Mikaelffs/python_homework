"""Exercise 1"""

"""Reads the contents in file1.txt, reformats them by adding the 
text Entry: before each line and produces a new file file2.txt"""

file2 = open("Python_Course/Exercise 2/exercises/files/file2.txt", "a+") #This creates the new file

with open("Python_Course/Exercise 2/exercises/files/file1.txt", "r") as file1: #This opens file1.txt as read-only and automatically closes it when it is done
	"""This loop iterates over the lines in file1 and stores the modified lines in file 2"""

	for line in file1: 
		file2.write("Entry: " + line)


"""Closes file2 to avoid problems"""
file2.close()

"""Exercise 2"""

chr = raw_input("Specify a chromosome between chr1 and chr20: ")

out = open("Python_Course/Exercise 2/exercises/files/out.txt", "a+")

with open("Python_Course/Exercise 2/exercises/files/genome.bed", "r") as file1:
	
	b = 0
	for line in file1:
		a = line.split()
		if a[0] == chr:
			out.write(a[0] + " " + a[1] + " " + a[2] + " " + "Fragment length: " + str(int(a[2]) - int(a[1])) + "\n")
			b +=1
	out.write("%s entires corresponding to %s" % (str(b), chr))


	# for line in file1:
	# 	if line[0:3] == chr:
	# 		out.write(line + "Fragment length: ")

out.close()

"""Exercise 3"""
"""This only works for trips going in one direction, so it's not that good"""

cities = ("New-York", "Geneva", "Paris")

with open("Python_Course/Exercise 2/exercises/files/distance.dat", "r") as file1:

	info = []

	for line in file1:
		info.append(line.split())

distance = 0

for city in range(0,len(cities)-1):
	for i in range(0,len(info)):
		if cities[city] == info[i][0] and cities[city + 1] == info[i][1]:
			distance += int(info[i][2])


print "The total distance is %s km" % (distance)

"""Exercise 4"""

"""4A"""
"""first version"""

def isrepetition(s1,s2):
	times = len(s1) / len(s2)

	if s1 == s2 * times:
		return True
	else:
		return False

"""smarter version"""

def isrepeititon(s1,s2):

	return s1 == s2 * (len(s1) / len(s2))

"""4B"""

def find_motif(s1):

	for i in range(1, len(s1)):
		motif = s1[0:i]

		if s1 == motif * (len(s1) / len(motif)):
			return motif

"""Exercise 5"""
"""SOlution to day2 exercise 5. This program opens three files
chrom.txt, start_end.txt and gene.txt. It produces a new file bed.txt
by combining the data from all three files"""


"""This opens all of the files and creates bed.txt as an empty file"""

chrom = open("Python_Course/Exercise 2/exercises/files/chrom.txt", "r")

start_end = open("Python_Course/Exercise 2/exercises/files/start_end.txt", "r")

gene = open("Python_Course/Exercise 2/exercises/files/gene.txt", "r")

bed = open("Python_Course/Exercise 2/exercises/files/bed.txt", "a+")

"""This creates three empty lists to fill with the data from the above files"""

chromlst = []
start_endlst = []
genelst = []

"""This adds the lines from the three files as elements of the lists"""

for line in chrom:
	chromlst.append(line)

for line in start_end:
	start_endlst.append(line)

for line in gene:
	genelst.append(line)

"""This combines the list elements corresponding to each line into a new file"""
for i in range(0,len(chromlst)):
 	bed.write(chromlst[i].rstrip("\n") + " " + start_endlst[i].rstrip("\n") + " " + genelst[i])



"""This closes all the files to complete the file manipulating instructions"""
chrom.close()
start_end.close()
gene.close()
bed.close()