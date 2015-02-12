import sys
import random

#mutations - cell replication, order and chaos coexist
#code via AParrish - http://www.decontextualize.com/teaching/rwet/simple-models-of-text/
for line in sys.stdin:
	line = line.strip()
	words = line.split(" ")
	random.shuffle(words)
	output = " ".join(words)
	print output

