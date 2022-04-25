
import linkedlist as mylist

def solution(l1,l2):

	i = 0
	carry = 0

	res = mylist.list()
	i = 0
	j = 0
	
	while(  l1 != None or l2 != None or carry):

		a = 0
		b = 0
		sum_digits = 0

		if l1 != None:
			a = l1.data
		if l2 != None:
			b = l2.data
		# print(f'a = {a},b {b}')
		sum_digits = a + b + carry 
		
		res.append(sum_digits % 10)

		if( l1 != None):
			l1 = l1.next
			i+=1

		if (l2 != None):
			l2 = l2.next
			j+=1

		carry = 0
		if sum_digits > 9 :
			carry = 1


	# if carry and i == j:
	# 	res.append(carry)
	return res


l1 = mylist.list(9)
l1.append(9)
l1.append(9)
l1.append(9)
l1.append(9)
l1.append(9)
l1.append(9)
# l1.append(9)

l2 = mylist.list(9)
l2.append(9)
l2.append(9)
l2.append(9)

print(l1.display())
print(l2.display())

l3 = solution(l1.get_head_ref(),l2.get_head_ref())

print(l3.display())
