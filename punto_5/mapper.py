import sys
for line in sys.stdin:
        words = line.split(',')
       	array=(words[2].split('-'))
	if("Date of Transfer"!=array[0]):	
		print(array[0]+"-"+array[1]+"\t"+str(1))
