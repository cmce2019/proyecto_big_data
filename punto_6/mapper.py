import sys
a=[]
for line in sys.stdin:
        words = line.split(',')	
	if(len(words)>7):
		if("Town/City"!=words[6]):	
			a.append(words[6]+"\t"+words[7])
