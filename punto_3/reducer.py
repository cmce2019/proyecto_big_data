import sys
data = sys.stdin.readlines()
aux=999999999
for linenum, line in enumerate(data):
        arr=line.replace("\n","").split("\t")
        if linenum == 0:
              count=int(arr[1])
              anterior=arr[0]
        else:
              if(anterior==arr[0]):
		    aux=int(arr[1])
		    if(aux<count):
	            	count=aux
              else:
                    print(anterior+" "+str(count))
                    anterior=arr[0]
                    count=int(arr[1])
print(anterior+" "+str(count))

