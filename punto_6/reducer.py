import sys
data = sys.stdin.readlines()
arr=set()
size= len(data)
for linenum, line in enumerate(data):
        arr=line.replace("\n","").split("\t")
        if arr[0]+"\t"+arr[1] not in arr:
            arr.add(arr[0]+"\t"+arr[1])
            print(arr[-1])
