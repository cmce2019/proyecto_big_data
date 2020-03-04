import sys
data = sys.stdin.readlines()
arr=[]
for linenum, line in enumerate(data):
    arr.append(int(line))
arr.sort()
for item in arr:
    print(item)