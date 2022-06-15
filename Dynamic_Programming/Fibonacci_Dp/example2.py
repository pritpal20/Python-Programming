

def fibonnaci(n):

	F = [0,1]


	for i in range(2,n+1):
		F.append(F[i -1]+ F[i -2])

	return F[n]


print(fibonnaci(500))


# for i in range(2,11):
# 	print(i)