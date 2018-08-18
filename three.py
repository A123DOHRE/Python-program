list = [32,34,67,90,34,98]
a=list
b=list
maxnumber = 0
for i in list:
	if i > maxnumber:
		maxnumber = i
print maxnumber 
max1=0
for value in a:
	if value > max1 and value!=maxnumber:
		max1 = value
print max1

max2=0
for value in b:
	if value > max2 and value!=max1 and value!=maxnumber:
		max2 = value
print max2












