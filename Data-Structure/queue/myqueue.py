class node:
	def __init__(self,data=None):
		self.data = data
		self.next = None


class MyQueue:
	'''
	Queue class
	'''

	def __init__(self):
		self.first = None
		self.last = None
		self.length = 0


 # (last) 1->2->3 ( first)
	def enqueue(self,data):
		
		new_node = node(data)
		if self.first == None:
			self.first = new_node
			self.last = new_node
		else:
			self.last.next = new_node
			self.last = new_node

		self.length+=1

	def deque(self):

		if self.length == 0 :
			return None
		
		temp = None
		if self.first == self.last:
			self.last = None
			temp = self.first
			self.first = None
		else:
			temp = self.first
			self.first = self.first.next

		self.length-=1
		return temp.data



	def peek(self):

		return self.first


que1 = MyQueue()

que1.enqueue('google')
que1.enqueue('Amazon')
que1.enqueue('Microsoft')
que1.enqueue('Apple')
que1.enqueue('Apple2')

print(que1.deque())
print(que1.deque())
print(que1.deque())
print(que1.deque())
print(que1.deque())
print(que1.deque())

que1.enqueue('TCS')
que1.enqueue('Accenture')
que1.enqueue('IBM')
que1.enqueue('CG')
que1.enqueue('NSE IT')

print(que1.deque())
print(que1.deque())
print(que1.deque())
print(que1.deque())
print(que1.deque())
print(que1.deque())

