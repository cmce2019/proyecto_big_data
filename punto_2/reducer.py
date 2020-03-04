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
    		    division=float(float(count)/float(size))
                    print(anterior+" "+str(division))
	            size=1
                    anterior=arr[0]
                    count=int(arr[1])
division=float(float(count)/float(size))
print(anterior+" "+str(division))
