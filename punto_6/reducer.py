import sys
data = sys.stdin.readlines()
size= len(data)
for linenum, line in enumerate(data):
        arr=line.replace("\n","").split("\t")
        if linenum == 0:
              count=1
              anterior=arr[0]
        else:
              if(anterior==arr[0]):
                    count=count+1
              else:
                    print(str(count)+"\t1"+anterior)
                    anterior=arr[0]
                    count=1
print(str(count)+"\t1"+anterior)
