

def isValid(s:str) -> bool :

	stack = ['N']

	dict_val = {']':'[','}':'{',')':'('}
	for i in s :

		if i in dict_val.keys():
			if stack.pop() != dict_val[i]:
				return False
		else:
			stack.append(i)

	if len(stack) == 1:
		return True

print(isValid("(])"))

