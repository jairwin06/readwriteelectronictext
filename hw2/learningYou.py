import random

#random.choice()
#random.sample()
#random.randrange()

beginnings = list()
for line in open("beginnings.txt"):
	line = line.strip()
	if len(line) > 0:
		beginnings.append(line)

deepLearning = list()
for line in open("deepLearning.txt"):
	line = line.strip()
	if len(line) > 0:
		deepLearning.append(line)

for i in range(12):
	rand_beginning = random.choice(beginnings)
	rand_deepLearning = random.choice(deepLearning)

	print rand_beginning + " " + rand_deepLearning