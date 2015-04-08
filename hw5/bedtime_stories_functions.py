
import random

#load files and assign list types
#this puts all the nouns in one list instead of creating a list of "noun"
#like in the other program
def load_file(fileName, type):
	type = list()

	for line in open(fileName):
		line = line.strip()
		if len(line) > 0:
			word_list.append(line)
			
		if type == peom_lines:
			peom_lines.append(line)

		if type == subject:
			subject.append(line)

		if type == noun:
			noun.append(line)

		if type == verb:
			verb.append(line)

		if type == gerund:
			gerund.append(line)

	return line

def random_choice(source_list, random_word):
	random_word = random_choice(source_list)
	return random_word


