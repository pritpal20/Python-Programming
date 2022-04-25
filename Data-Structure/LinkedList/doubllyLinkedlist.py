import sys 

class node(object):
	def __init__(self,data):
		self.data = data
		self.next = None
		self.prev = None


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

		new_node = node(data)

		if self.head == None:
			self.head = new_node
			self.tail = self.head
		
		self.tail.next = new_node
		new_node.prev = self.tail
		self.tail = new_node

		self.length+=1

	def push(self,data):
		current = node(data)
		current.next = self.head
		self.head = current
		self.length+=1

	def getPreviousNode(self,index):

		if index < 0 :
			return None
		count = 0

		current = self.head
		while(count != index):
			current = current.next
			count+=1

		return current


	# insert element at the index
	def insert(self,index,data):

		if index >= self.length:
			self.append(data)
			self.print()
			return
		
		new_node = node(data)
		
		if index == 0 :
			new_node.next = self.head
			self.head.prev = new_node
			self.head = new_node
			self.length+=1
			self.print()
			return


		previousNode = self.getPreviousNode(index-1)

		holdingPointer = previousNode.next
		previousNode.next = new_node
		new_node.next = holdingPointer
		holdingPointer.prev = new_node
		new_node.prev = previousNode

		self.length+=1

		self.print()
		

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

		while current.next != None:
			# temp.append(current.data)
			print(f'{current.data}',end='-->')
			current = current.next

		# temp.append(current.data)
		print(f'{current.data}',end='-->NULL\n')
		# return temp

	def len(self):
		
		return self.length

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
	def delete(self,index):
		
		if index >= self.length:
			print('ERROR !!! Out of index')
			return

		currentNode = None 
		nextNode = None
		previousNode = self.getPreviousNode(index-1)

		if index == self.length -1:
			print('Last elememt deleted')
			self.tail = previousNode

		if previousNode != None:
			currentNode = previousNode.next
			nextNode = currentNode.next
			previousNode.next = nextNode

		else:
			currentNode = self.head
			self.head = currentNode.next

		

		
		del currentNode

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

	def reverse(self):

		current = self.tail

		while(current):

			print(current.data,end='-->')
			current = current.prev

		print("NULL\n")




def main(argv):

	mylist = list('0')

	for i in range(1,11):
		mylist.append(i)

	mylist.print()
	print(mylist.len())
	print(mylist.__dict__)

	# mylist.delete(1)
	mylist.insert(0,11)
	mylist.print()
	print(mylist.tail.prev.data)

	mylist.reverse()



if __name__ == '__main__':

	main(sys.argv)


