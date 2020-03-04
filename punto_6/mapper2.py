import sys
a=[]
for line in sys.stdin:
    words = line.split('\t')
    print(words[0].replace("\n","")+"\t"+words[1])

	
