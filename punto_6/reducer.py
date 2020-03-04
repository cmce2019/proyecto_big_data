import sys
data = sys.stdin.readlines()
districts = {}
for linenum, line in enumerate(data):
        arr=line.replace("\n","").split("\t")
        if linenum == 0:
              districts[arr[0]]=1
        else:
              if(arr[0] in districts):
                    districts[arr[0]]=1+districts[arr[0]]
              else:
                    districts[arr[0]]=1
for key in districts:
      print (str(districts[key])+"\t1")
