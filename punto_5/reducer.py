import sys
data = sys.stdin.readlines()
months_count=[]
def init(array):
	array[:]=[] 
	for i in range(0,12):
		array.append(1)
def pos(num,array):
	for i in range(0,12):
		if(num==array[i]):
			return i+1


for linenum, line in enumerate(data):
        arr=line.replace("\n","").split("\t")
        if (linenum == 0):
              last_year=arr[0]
              init(months_count)
        else:
              if(last_year==arr[0]):
                        months_count[int(arr[1])-1]=1+months_count[int(arr[1])-1]
              else:
		    aux_arr=months_count[:]
		    aux_arr.sort(reverse=True)
                    print(last_year+" "+str(pos(aux_arr[0],months_count)))
                    last_year=arr[0]
		    init(months_count)
aux_arr=months_count[:]
aux_arr.sort(reverse=True)
print(last_year+" "+str(pos(aux_arr[0],months_count)))
