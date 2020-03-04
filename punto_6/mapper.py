import sys
a=[]
for line in sys.stdin:
        words = line.split(',')	
	if(len(words)>8):
		if("Town/City"!=words[6] and not(str(words[8]+"\t"+words[6]) in a)):	
			a.append(words[8]+"\t"+words[6])
			print(words[8]+"\t1")
	
