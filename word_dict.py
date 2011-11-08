fo = open('z.py','r')
count = 0
word_dict = {}
text= fo.readlines()
for line in text:
    line = line.lower()
    count = count + 1
    #print line,count, #
    for word in line.split():
        #print word #
        freq = (line.split()).count(word)
        print freq ,word        #
    