import sys
import random

#coming into existence, all does not begin and end at this moment; 
#not yet fully conscious, you pick up only snippets of your environment
for line in sys.stdin:
	line = line.strip()

	randLow = random.randint(0, 10)
	randHigh = random.randint(11, 20)

	print line[randLow:randHigh]