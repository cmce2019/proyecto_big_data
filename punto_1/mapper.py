import sys
for line in sys.stdin:
        words = line.split(',')
       	array=(words[2].split('-')[0])
	if("Date of Transfer"!=array):	
		print(array+"\t"+str(1))
