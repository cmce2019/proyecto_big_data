import sys
a=[]
for line in sys.stdin:
        words = line.split(',')	
	if(len(words)>7):
		if("Town/City"!=words[6] and (str(words[6]+"\t"+words[7]) not in a)):	
			a.append(words[6]+"\t"words[7])
			print(a[-1])
