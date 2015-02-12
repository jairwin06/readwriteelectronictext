import sys

#all_lines = list()

#find lines with the word "my" or "your"
for line in sys.stdin:
	line = line.strip()
	#all_lines.append(line)
	my = line.find("my")
	your = line.find("your")

	if my != -1: 
		mywords = line.split(" ")  #returns a list
		ind = mywords.index("my")  #returns an int
		next = mywords.index("my") + 1
		
		for i, v in enumerate(mywords):
			if i == ind:
				print v
			if i == next:
				print v
			

	if your != -1: 
		yourwords = line.split(" ")  #returns a list
		indy = yourwords.index("your")  #returns an int
		nexty = yourwords.index("your") + 1
		
		for i, v in enumerate(yourwords):
			if i == indy:
				print v
			if i == nexty:
				print v

	
		
		