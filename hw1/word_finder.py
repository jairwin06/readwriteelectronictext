import sys

#word-finder
for line in sys.stdin:
	line = line.strip()
	my = line.find("my ")
	your = line.find("your")
	if my != -1: 
		print line[my:my+12]
	if your != -1:
		print line[your:your+12]