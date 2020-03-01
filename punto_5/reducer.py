import sys
data = sys.stdin.readlines()
for linenum, line in enumerate(data):
        arr=line.replace("\n","").split("\t")
	aux_arr=arr[0].split("-")
        if linenum == 0:
	      last_count=1
              count=1
              last_year=aux_arr[0]
	      last_month=aux_arr[1]
	      curr_month=aux_arr[1]
        else:
              if(last_year==aux_arr[0]):
		    if(last_month==aux_arr[1]):
                    	count=count+1
		    else:
			if(count>last_count):
				last_count=count
				curr_month=last_month
			count=1
			last_month=aux_arr[1]
              else:
                    print(last_year+" "+curr_month)
                    last_year=aux_arr[0]
		    last_month=aux_arr[1]
                    last_count=1
if(count>last_count):
	last_count=count
	curr_month=last_month
print(last_year+" "+curr_month)
