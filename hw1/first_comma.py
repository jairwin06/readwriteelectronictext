import sys

for line in sys.stdin:
	line = line.strip()
	space_posiiton = line.find(", ")
	if space_posiiton != -1:
		substring = line[space_posiiton+1:]
		print substring