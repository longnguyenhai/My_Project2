# In put a file
fo = open('z.py','r')
#line = fo.readlines()'
count = 0
for line in fo:
	line  = (line.strip()).split()
	#print line
	count = count +1
	for word in line:
		freq=line.count(word)
		print freq,word,count




