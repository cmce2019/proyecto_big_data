import sys
data = sys.stdin.readlines()
arr=[]
size= len(data)
for linenum, line in enumerate(data):
        arr=line.replace("\n","").split("\t")
        if (str(arr[0]+"\t"+arr[1]) not in arr):
            arr.append(arr[0]+"\t"+arr[1])
            print(arr[-1])
