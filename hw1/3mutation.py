import sys
import random

#what is being born like?
for line in sys.stdin:
	line = line.strip()
	words = line.split(" ")
	random.shuffle(words)
	output = " ".join(words)
	print output

