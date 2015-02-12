import sys

#word-finder by splitting lines
for line in sys.stdin:
	line = line.strip()

	my = line.find("my ")
	me = line.find("me ")
	mine = line.find("mine ")
	eye = line.find("I ")
	myself = line.find("myself ")

	if my != -1: 
		print line[my:]
	if me != -1:
		print line[me:]
	if mine != -1:
		print line[mine:]
	if eye != -1:
		print line[eye:]
	if myself != -1:
		print line[myself:]


	



