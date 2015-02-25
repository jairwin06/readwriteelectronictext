#import sys
import random


#open and split the lines in the file
input = open("results.txt")
input_string = open("results.txt").read() 
input_words = input_string.split()

keys = open("definitions_keys2.txt")
vals = open("definitions_values2.txt")

definitions_keys = list()
for line in keys:
	line = line.strip()
	definitions_keys.append(line)

definitions_vals = list()
for line in vals:
	line = line.strip()
	definitions_vals.append(line)

poem_lines = list()
for line in input:
	line = line.strip()
	poem_lines.append(line)


for i in range(12):
	r = random.randint(1,10)
	b = random.randint(1,5)
	print poem_lines[i]
	if r in range(4):
		if b < 3:
			print "But that would mean it's"
		print definitions_keys[i]
	if r in range(8):
		if b < 4:
			print "So that means it's"
		print definitions_vals[i]


	


