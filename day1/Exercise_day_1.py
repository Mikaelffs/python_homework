"""Exersice 1"""

def vowels(my_string):
	
	s1 = 0
	s2 = ""

	for i in my_string.lower():
		if i in ["a", "e", "i", "o", "u", "y"]:
			s1 += 1
		if i in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
			s2 = "There are numbers!"

	return ["There are %s vowels" % s1, s2]

print vowels("abga")

"""Exersice 2"""

s = 2
while s <= 10:
	print s
	s += 2
else: 
	print "Goodbye!

"""Exersice 3"""

for i in range(2,11):
	if i % 2 == 0:
		print i
	if i >= 10:
		print "Goodbye!"

"""Exersice 4"""

#A) Each thing is printed as many times as 
#it appears in the string, done is printed once afterwards

#B) H: 1 E: 2 L: 3 O: 1 !: 2 Done: 1

#C) p: 2 o: 0 num_vowels: 3 num_cons: -2

"""Exersice 5"""

def count_bob(my_string):
	bob = 0

	for i in range(0,len(my_string)-2):
		if my_string[i] + my_string[i+1] + my_string[i+2] == "bob":
			bob += 1
	return bob

print count_bob("bobkfsdgidigbobksdyfjg")

"""Exersice 6"""

"""I could not figure this one out on my own so I looked at the solution, 
I was trying to do it in too short of a format"""

"""Exersice 7"""

def count_bob(my_string, my_string2):
	bob = 0

	for i in range(0,len(my_string)-2):
		if my_string[i] + my_string[i+1] + my_string[i+2] == my_string2:
			bob += 1
	return bob

print count_bob("bobkfsdgidigbobksdyfjg")