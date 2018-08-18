def palindrom(lower,upper):
	for num in range(lower,upper,+1):
		con=list(str(num))
		if con[::-1]==con:
			print "".join(con)
num=palindrom(1,1000)
print (num)

