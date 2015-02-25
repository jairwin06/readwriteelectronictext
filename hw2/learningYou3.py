import random

#original attempt to use a dictionary - this attempt was unsuccessful and the code is a WIP

#create a dictionary:
definitions = {
	'a lady': 'a well-mannered and considerate woman with high standards of proper behavior',
	'a banana': 'an elongated, edible fruit, having a thick yellowish skin and white pulp',
	'a haircut': 'a style in which hair is cut',
	'a girl': 'a female child',
	'a shirt': 'a garment for the upper part of the body',
	'a video game': 'a game played against a computer',
	'a hand': 'the terminal part of the human arm used for grasping and holding',
	'a face': 'the surface of the front of the head from the top of the forehead to the base of the chin and from ear to ear',
	'a woman': 'an adult female human',
	'a smile': 'a facial expression characterized by an upward curving of the corners of the mouth and indicating pleasure, amusement, or derision',
	'a hairdo': 'the arrangement of the hair (especially a woman\'s hair)',
	'a wig': 'an artificial covering of human or synthetic hair',
	'a breast': 'either of two milk-secreting, glandular organs on the chest of a woman',
	'a pigtail': 'a cue formed of the hair of the head, as distinguished from that of the periwig',
	'a leotard': 'a tight-fitting garment of stretchy material that covers the body from the shoulders to the thighs',
	'sucking': 'deriving nourishment from the mother\'s breast',
	'holding': 'the act or state of sustaining, grasping, or retaining',
	'wearing': 'the act of having on your person as a covering or adornment'
}

input = open("results.txt")
input_string = open("results.txt").read() 
input_words = input_string.split()

for line in input:
	line = line.strip()

	defs_keys = list()
	defs_vals = list()

	for word in input_words:
		if word in definitions.keys():
			defs_keys.append(word)
			defs_vals.append(word)
			
	if defs_vals > 0:
		for i in range(12):
			print line[i]
			print defs_keys[i]
			print defs_vals[i]

