class node:
	def __init__(self,data=None):
		self.data = data
		self.left = None 
		self.right = None 


class tree:
	def __init__(self,data=None):

		self.root = None


	def insert(self,data):

		new_node = node(data)
		if self.root == None:
			self.root = new_node
		else:
			currentNode = self.root
			while(True):

				if data < currentNode.data :
					# left 
					if currentNode.left == None:
						currentNode.left = new_node
						return self
					currentNode = currentNode.left
				else :
					# right 
					if currentNode.right == None:
						currentNode.right = new_node
						return self
					currentNode = currentNode.right

	def search(self,value):
		pass



bst1 = tree()

bst1.insert(9)
bst1.insert(4)
bst1.insert(20)
bst1.insert(15)
bst1.insert(130)
bst1.insert(100)
bst1.insert(6)

print(bst1.root.right.right.left.__dict__)
