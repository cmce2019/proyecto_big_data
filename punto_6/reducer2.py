import sys
data = sys.stdin.readlines()
districts = {}
for linenum, line in enumerate(data):
        arr=line.replace("\n","").split("\t")
        if linenum == 0 and arr[0]!='':  
              districts[arr[0]]=int(arr[1])
        else:
              if(arr[0] in districts and arr[0]!=''):
                    districts[arr[0]]=int(arr[1])+districts[arr[0]]
              elif arr[0]!='':
                    districts[arr[0]]=int(arr[1])
for key in districts:
      print (str(districts[key])+"\t"+str(key))
