import sys
a=[]
for line in sys.stdin:
        words = line.split(',')	
	if(len(words)>7):
		if( "Town/City"!=words[6] and not(str(words[7]) in a)):	
			a.append(words[7])
			print(words[6]+"\t1")
print(len(a))
	
