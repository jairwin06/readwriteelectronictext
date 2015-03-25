import random

is_list = list()
for line in open('is.txt'):
	line = line.strip()
	if len(line) > 0:
		is_list.append(line)

does_list = list()
for line in open('does.txt'):
	line = line.strip()
	if len(line) > 0:
		does_list.append(line)

means_list = list()
for line in open('means.txt'):
	line = line.strip()
	if len(line) > 0:
		means_list.append(line)

gerunds = list()
for line in open('gerunds.txt'):
	line = line.strip()
	if len(line) > 0:
		gerunds.append(line)

jobs = list()
for line in open('jobs.txt'):
	line = line.strip()
	if len(line) > 0:
		jobs.append(line)

news_topics = list()
for line in open('news_topics.txt'):
	line = line.strip()
	if len(line) > 0:
		news_topics.append(line)

nouns_that_are_verbs = list()
for line in open('nouns_that_are_verbs.txt'):
	line = line.strip()
	if len(line) > 0:
		nouns_that_are_verbs.append(line)

pet_supplies = list()
for line in open('pet_supplies.txt'):
	line = line.strip()
	if len(line) > 0:
		pet_supplies.append(line)

scope = list()
for line in open('scope.txt'):
	line = line.strip()
	if len(line) > 0:
		scope.append(line)

sporting_goods = list()
for line in open('sporting_goods.txt'):
	line = line.strip()
	if len(line) > 0:
		sporting_goods.append(line)

verbs = list()
for line in open('verbs.txt'):
	line = line.strip()
	if len(line) > 0:
		verbs.append(line)

noun_lists = list()
noun_lists.append(jobs)
noun_lists.append(news_topics)
noun_lists.append(nouns_that_are_verbs)
noun_lists.append(pet_supplies)
noun_lists.append(scope)
noun_lists.append(sporting_goods)

source_list = random.choice(noun_lists)

subject_word = random.choice(source_list)
three = random.choice(random.choice(noun_lists))
four = random.choice(random.choice(noun_lists))
six = random.choice(random.choice(noun_lists))
seven = random.choice(random.choice(noun_lists))
eight = random.choice(random.choice(noun_lists))
nine = random.choice(random.choice(noun_lists))
verb = random.choice(verbs)
gerund = random.choice(gerunds)

#stanza 1: what it is; binary relationships
for line in is_list:
	line_words = line.split()
	#x = random.choice(random.choice(noun_lists))
	one = random.choice(random.choice(noun_lists))
	two = random.choice(random.choice(noun_lists))
	five = random.choice(random.choice(noun_lists))
	
	
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

	print line 





