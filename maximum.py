list = [23,45,54,98,78]
maxnumber= list[0]
minVal = list[0]
for i  in range(0,len(list),1):
	maxnumber = max(maxnumber,list[i])
	minVal = min(minVal,list[i])
print ("max:",maxnumber)
print ("min:",minVal)
