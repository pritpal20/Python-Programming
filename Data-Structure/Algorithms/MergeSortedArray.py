
#Test case 1
L1 = [2,3,5,8,10,11,12,13]
L2 = [4,6,7,9,15]

#Test case 2 
# L1 = []
# L2 = []


def MergeSortedArrays(A,B):

	len_A = len(A)
	len_B = len(B)
	
	i =0
	j = 0
	SortedArray = []
	while( i < len_A and j < len_B):


		if A[i] < B[j] :
			SortedArray.append(A[i])
			i+=1
		else:
			SortedArray.append(B[j])
			j+=1

	# Any element remaining is added to list
	for i in range(i,len_A):
		SortedArray.append(A[i])

	# Any element remaining is added to list
	for j in range(j,len_B):
		SortedArray.append(B[j])

	return SortedArray


print(MergeSortedArrays(L1,L2))