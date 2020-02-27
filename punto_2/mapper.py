import sys
for line in sys.stdin:
        words = line.split(',')
	if("Town/City"!=words[6]):	
		print(words[6]+"\t"+str(words[1]))
