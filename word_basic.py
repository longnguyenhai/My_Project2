# In put a file
file_input = raw_input ("File input:")
fo = open(file_input,'r')
count = 0
word_list = []
for line in fo:
	line  = (line.strip()).split()          # strip white space and split word to a list
	count = count +1                      # count line
	for word in line:
		word= word.lower()            # lower word
		freq=line.count(word)        #  count frequence word 
		for elem in word_list:
			if elem[0] == word:
				elem[1] += 1
				if count not in elem[2]:
					elem[2].append(count)
				break
		else:
			word_list.append( [word,freq,[count]] )
            
for i in word_list:
	print "%2d %s %d %d" %(i[1],i[0], i[2][0], i[2][1])
