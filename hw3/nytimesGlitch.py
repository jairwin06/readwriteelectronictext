import random

#read file contents into strings
#from aparrish
nytimes = open("articleSearch.txt").read()

for i in range(10):
	article_start = random.randrange(len(nytimes))
	article_length = random.randrange(8,20)
	article_fragment = nytimes[article_start : article_start + article_length]

	print article_fragment
