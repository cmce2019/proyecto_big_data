import sys
for line in sys.stdin:
        words = line.split(',')
        array=(words[2].split('-')[0])
        if("Date of Transfer"!=array and array=="1995" and words[6]=="STAMFORD"):
                print(str(words[1]))


