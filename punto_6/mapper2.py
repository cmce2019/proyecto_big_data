import sys
a=[]
for line in sys.stdin:
    words = line.split('\t')	
    print(words[0]+"\t"+words[1])
	
