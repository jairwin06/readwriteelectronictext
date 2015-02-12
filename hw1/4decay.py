import sys
import random

#word-finder by splitting lines
for line in sys.stdin:
	line = line.strip()

	low = random.randint(2, 8)
	high = random.randint(-8, -2)
	
	beginning = line[:low]
	ending = line[high:]

	print beginning + ending