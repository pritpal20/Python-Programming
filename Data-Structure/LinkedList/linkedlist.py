import sys 

class node(object):
	def __init__(self,data):
		self.data = data
		self.next = None


class list(object):

	def __init__(self,data=None):
		self.head = node(data)
		self.tail = self.head
		self.length = 1

	def append_old(self,data):
		current = self.head

		while current.next != None:
			current = current.next

		current.next = node(data)
		self.length+=1

	def append(self,data):

		new_node = None
		if self.head.data != None:
			new_node = node(data)
		else:
			self.head.data = data
			return 

		if self.head == None:
			self.head = new_node
			self.tail = self.head
		
		self.tail.next = new_node
		self.tail = new_node

		self.length+=1

	def push(self,data):
		current = node(data)
		current.next = self.head
		self.head = current
		self.length+=1

	def getPreviousNode(self,index):

		count = 0

		current = self.head
		while(count != index):
			current = current.next
			count+=1

		return current


	# insert element at the index

	def insert_new(self,index,data):

		if index >= self.length:
			self.append(data)
			self.print()
			return
		
		new_node = node(data)
		
		if index == 0 :
			new_node.next = self.head
			self.head = new_node
			self.length+=1
			self.print()
			return


		previousNode = self.getPreviousNode(index-1)

		holdingPointer = previousNode.next
		previousNode.next = new_node
		new_node.next = holdingPointer

		self.length+=1

		self.print()

	# def insert(self,index,data):

	# 	if index >= self.length:
	# 		print('ERROR !!! Out of index')
	# 		self.append(data)
	# 		return

	# 	count = 0 
	# 	temp_node = node(data)
	# 	current = self.head
	# 	previous = None

	# 	while current.next != None:

	# 		if index == count:
	# 			break
			
	# 		previous = current
	# 		current = current.next
	# 		count+=1

	# 	if previous != None:
	# 		previous.next = temp_node
	# 	else:
	# 		self.head = temp_node

	# 	temp_node.next = current
	# 	self.length+=1
		

	def display(self):
		temp = []
		current = self.head

		if current == None:
			return temp
		
		while current.next != None:
			temp.append(current.data)
			current = current.next

		temp.append(current.data)
		return temp

	def print(self):
		
		current = self.head
		if current == None:
			print('NULL')
			# return temp

		# print('head',end='\n')
		# print('head-->',end=' ')
		print("[",end='')
		while current.next != None:
			# temp.append(current.data)
			print(f'{current.data}',end=',')
			current = current.next

		# temp.append(current.data)
		print(f'{current.data}',end=']\n')
		# return temp

	def len(self):
		
		return self.length

		# alternate implementation
		# item_count = 0
		# current = self.head
		# while current.next != None:
		# 	current = current.next
		# 	item_count+=1

		# return item_count+1


	def get(self,index):

		if index >= self.length:
			print('ERROR !!! Out of index')
			return None

		current = self.head

		count = 0 
		while current.next != None:

			if index == count:
				return current.data
			current = current.next
			count+=1

		return current.data

	# [1,2,3,]
	# erase(1)
	# [1,3]
	def erase(self,index):
		
		if index >= self.length:
			print('ERROR !!! Out of index')
			return

		count = 0 
		current = self.head
		previous = None
		while current.next != None:

			if index == count:
				break
			
			previous = current
			current = current.next
			count+=1


		if previous != None:
			previous.next = current.next
		else:
			self.head = current.next

		# print(f'Deleting element {current.data} at index {index}')
		
		del current

		if index == self.length -1:
			print('Last elememt deleted')
			self.tail = previous

		self.length-=1

	def middle_element(self):

		if self.length == 0 :
			return None
		slow = self.head
		fast = self.head

		while(fast.next != None):

			if fast.next.next == None:
				break
			slow = slow.next
			fast = fast.next.next

		return slow.data

	def get_head_ref(self):
		return self.head

	def removeNthElement(self,index):

		ptr_temp = self.head 
		ptr_nth = self.head

		i = 0
		while(i < index):

			ptr_temp = ptr_temp.next
			i+=1

		if ptr_temp == None:
			return None

		prev = None

		print('ptr_temp.data',ptr_temp.data)
		while(ptr_temp != None):
			prev = ptr_nth
			ptr_temp = ptr_temp.next
			ptr_nth = ptr_nth.next

		if prev == self.head :
			print("Yes")
			self.head = self.head.next
		else:
			prev.next = ptr_nth.next

		print(ptr_nth.data)
		return ptr_nth



def AddtoDict(D_element,Key,Value):

	try :
		D_element[Key]  = Value
	except KeyError:
		D_element[Key] = Value

	return D_element


def GetElement(D_element,Key):
	try :
		if D_element[Key]  == True:
			return True
		
	except KeyError:
		return False

	return D_element


def main(argv):

	mylist = list(0)

	for i in range(1,4):
		mylist.append(i)

	mylist.print()
	# print(mylist.tail.data)
	# print(mylist.__dict__)
	# mylist.erase(0)
	# mylist.insert_new(13,99)
	# print(mylist.len())

	# mylist.tail.next = mylist.head

	# current = mylist.head

	# my_dict = {}
	# while(current != None):


	# 	print("current.data",id(current))
	# 	AddtoDict(my_dict,id(current),True)

	# 	if current.next != None:
	# 		if GetElement(my_dict,id(current.next)):
	# 			print('List is cirular')
	# 			# exit(0)
	# 			break

	# 	current = current.next


	# print(my_dict)
	# print('List is not circular')



	# print(mylist.removeNthElement(4).data)
	mylist.print()


		


if __name__ == '__main__':

	main(sys.argv)


