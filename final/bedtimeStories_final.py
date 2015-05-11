
#takes a text and gives a 
from textblob import TextBlob
from textblob import Word
import sys
import random

poetic_form = list()
for line in open('poeticForm.txt'):
	line = line.strip()
	if len(line) > 0:
		poetic_form.append(line)

text = sys.stdin.read().decode('ascii', errors="replace")
blob = TextBlob(text)

noun_phrases = blob.noun_phrases

verbs = list()
for word, tag in blob.tags:
	if tag == 'VB':
		verbs.append(word.lemmatize())

subject_word = random.choice(noun_phrases)

#for line in blob:
	#line = line.strip()
	#line = line.decode('ascii', errors="replace")
	#words = line.split(" ")
	#output = list()
	#for word_str in words:
		#word_obj = Word(word_str)
		#if len(word_str) > 3 and len(word_obj.synsets) > 0:
			#random_synset = random.choice(word_obj.synsets)
			#random_lemma = random.choice(random_synset.lemma_names)
			#output.append(random_lemma.replace('_', ' '))
		#else:
			#output.append(word_str)


three = random.choice(noun_phrases)
four = random.choice(noun_phrases)
six = random.choice(noun_phrases)
seven = random.choice(noun_phrases)
eight = random.choice(noun_phrases)
nine = random.choice(noun_phrases)
verb = random.choice(verbs)
gerund = random.choice(verbs)

#stanza 1: what it is; binary relationships
for line in poetic_form:
	line_words = line.split()
	#x = random.choice(random.choice(noun_lists))
	one = random.choice(noun_phrases)
	two = random.choice(noun_phrases)
	five = random.choice(noun_phrases)
	
	
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
		line = line.replace('gerund', gerund+'ing')

	if 'verb' in line:
		line = line.replace('verb', verb+'s')

	print line 

