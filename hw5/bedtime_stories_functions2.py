import random

main_poem = list()
noun_list = list()
verb_list = list()
gerund_list = list()

def import_file(file_name, type):
	type = list()	

	for line in open(file_name):
		line = line.strip()
		
		if len(line) > 0:
			type.append(line)

	return type

def repeating_word_selection():
	is_list = import_file('is.txt', main_poem)

	verb = random.choice(import_file('verbs.txt', verb_list))
	gerund = random.choice(import_file('gerunds.txt', gerund_list))

	noun_list.append(import_file('jobs.txt', noun_list))
	noun_list.append(import_file('news_topics.txt', noun_list))
	noun_list.append(import_file('nouns_that_are_verbs.txt', noun_list))
	noun_list.append(import_file('pet_supplies.txt', noun_list))
	noun_list.append(import_file('scope.txt', noun_list))
	noun_list.append(import_file('sporting_goods.txt', noun_list))


def fill_in_words():
	repeating_word_selection()

	subject_word = random.choice(noun_list)
	three = random.choice(noun_list)
	four = random.choice(noun_list)
	six = random.choice(noun_list)
	seven = random.choice(noun_list)
	eight = random.choice(noun_list)
	nine = random.choice(noun_list)

	for line in is_list:
		line_words = line.split()
		one = random.choice(noun_list)
		two = random.choice(noun_list)
		five = random.choice(noun_list)

		if 'subject' in line:
			line = line.replace('subject', subject_word)

		if 'one' in line:
			line = line.replace('one', one)

		if 'two' in line:
			line = line.replace('two', two)

		if 'three' in line:
			line = line.replace('three', three)

		if 'four' in line:
			line = line.replace('four', four)

		if 'five' in line:
			line = line.replace('five', five)

		if 'six' in line:
			line = line.replace('six', six)	

		if 'seven' in line:
			line = line.replace('seven', seven)

		if 'eight' in line:
			line = line.replace('eight', eight)

		if 'nine' in line:
			line = line.replace('nine', nine)

		if 'gerund' in line:
			line = line.replace('gerund', gerund)

		if 'verb' in line:
			line = line.replace('verb', verb)

	return line 


print fill_in_words()