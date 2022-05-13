# First recurring number in the list 

def AddtoDict(D_element,element):

	try :
		D_element[element] +=1
	except KeyError:
		D_element[element] = 1

	return D_element


def find_first_recurring_num(A):
	A_hash = {}

	for item in A:

		AddtoDict(A_hash,item)
		if A_hash[item] == 2:
			return item
	return

A1 = [2,3,3,8,2,8,7]


print(find_first_recurring_num(A1))