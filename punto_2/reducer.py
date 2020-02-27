import sys
data = sys.stdin.readlines()
size= 1
for linenum, line in enumerate(data):
        arr=line.replace("\n","").split("\t")
        if linenum == 0:
	      size=1
              count=int(arr[1])
              anterior=arr[0]
        else:
              if(anterior==arr[0]):
		    size=size+1
                    count=count+int(arr[1])
              else:
                    print(anterior+" "+str(count)+"/"+str(size))
	            size=1
                    anterior=arr[0]
                    count=int(arr[1])
print(anterior+" "+str(count)+"/"+str(size))
