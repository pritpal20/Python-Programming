import sys 

class node(object):
	def __init__(self,data):
		self.data = data
		self.next = None

	def __repr__(self):

		return f"{self.data}->{self.next}"


class list(object):

	def __init__(self,data=None):
		self.head = node(data)
		self.tail = self.head
		self.length = 1

	def __repr__(self):

		return f'\n[head = {self.head.data},length = {self.length}] \n{self.head.data}->{self.head.next} \n[tail = {self.tail}] '

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
		while current.next != None:
			# temp.append(current.data)
			print(f'{current.data}',end='-->')
			current = current.next

		# temp.append(current.data)
		print(f'{current.data}',end='-->NULL\n')
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

	# 1->2->3->4->NULL
	# N = 2 
	# 1->2->4>NULL
	def removeNthElement(self,N):

		ptr_temp = self.head
		ptr_Nth = self.head

		index = 0 
		prev = None
		while(ptr_temp != None):

			if index == N:
				break;
			ptr_temp = ptr_temp.next 

			index+=1

		while(ptr_temp != None):

			prev = ptr_Nth
			ptr_Nth = ptr_Nth.next
			ptr_temp = ptr_temp.next

		# print(prev)
		# print(ptr_Nth)
		self.length-=1
		if prev != None:
			prev.next = ptr_Nth.next
			return ptr_Nth.data
		else:
			self.head = self.head.next 
			return None







def main(argv):

	mylist = list()

	for i in range(1,6):
		mylist.append(i)

	# mylist.print()
	# print("lenght of list",mylist.len())

	print(mylist)

	print(mylist.removeNthElement(6))
	# mylist.print()
	print(mylist)




if __name__ == '__main__':

	main(sys.argv)


