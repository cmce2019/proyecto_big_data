import sys
a=[]
for line in sys.stdin:
        words = line.split(',')	
	if("Town/City"!=words[6] and (str(words[6]+"\t"+words[7]) not in a)):	
		a.append(words[6]+"\t1")
		print(a[-1])
