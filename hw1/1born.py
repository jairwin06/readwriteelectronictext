import sys
import random

#what is growing up like
for line in sys.stdin:
	line = line.strip()

	randLow = random.randint(0, 10)
	randHigh = random.randint(11, 20)

	print line[randLow:randHigh]