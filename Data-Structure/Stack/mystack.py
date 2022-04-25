
class node(object):
	def __init__(self,data=None):
		self.data = data
		self.next = None


class MyStack:
	
	def __init__(self):
		self.top = None 
		self.bottom = None 
		self.length = 0

	def push(self,data):

		new_node = node(data)

		if self.top == None:
			self.top = new_node
			self.bottom = self.top
			return

		temp = self.top 
		self.top = new_node
		new_node.next = temp

		self.length+=1

	def isempty(self):

		if self.length == 0:
			return true

		return False

	def peek(self):

		if self.isempty():
			return None

		return self.top

	def pop(self):

		temp = self.top
		self.top = self.top.next
		return temp.data


stack1 = MyStack()

stack1.push('A')
stack1.push('B')
stack1.push('C')

print(stack1.__dict__)

print(stack1.pop())

print(stack1.pop())
print(stack1.peek())

