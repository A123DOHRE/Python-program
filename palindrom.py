lower=1
upper=1000
for num in range(lower,upper,+1):
	con=list(str(num))
	if con[::-1]==con:
		print "".join(con)
					
