class node:
	def __init__(self,data=None):
		self.data = data
		self.left = None 
		self.right = None 


class tree:
	def __init__(self,data=None):

		self.root = None


	def insert2(self,data):

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
		
		if self.root == None:
			return None
		else:
			currentNode = self.root
			while(True):
				print(f'currentNode.data {currentNode.data} value {value}')
				if currentNode.data > value:

					currentNode = currentNode.left
					if currentNode == None:
						return None 
				elif currentNode.data < value :

					print('here')
					currentNode = currentNode.right
					if currentNode == None:
						return None 
				elif currentNode.data == value:
					return currentNode


	def remove2(self,value):

		if self.root == None:
			return None
		else:
			currentNode = self.root

			while(True):
				# print(f'currentNode.data {currentNode.data} value {value}')
				if currentNode.data > value:

					currentNode = currentNode.left
					if currentNode == None:
						return None 
				elif currentNode.data < value :

					# print('here')
					currentNode = currentNode.right
					if currentNode == None:
						return None 
				elif currentNode.data == value:
					# print('Hello')
					temp = currentNode
					if currentNode.right != None:
						currentNode = currentNode.right
					
					elif currentNode.left != None:
						currentNode = currentNode.left

						print(f'currentNode.data {currentNode} {currentNode.right} ')
						return self
					else:
						currentNode = None
					
					print(f'deleting the node {temp} with data {temp.data}')
					del temp	
					print(temp)
					return self

		return None

	def insert(self,value):

		self.root = self.insert_node(self.root,value)


	def insert_node(self,node_ptr,value):

		# base case when root is empty 
		if node_ptr == None:
			return node(value)

		if value < node_ptr.data:
			node_ptr.left = self.insert_node(node_ptr.left,value)

		if value > node_ptr.data:
			node_ptr.right = self.insert_node(node_ptr.right,value)

		return node_ptr

	def traverse(self,currentNode=None):

		# currentNode = self.root
		if currentNode == None:
			return None

		curr = currentNode.data
		left = None
		right = None
		if currentNode.left != None:
			left = currentNode.left.data
		if currentNode.right != None:
			right = currentNode.right.data
		print(f"     [{currentNode.data} {currentNode}]") 
		print(f"[{left}]    [{right}] ")

		self.traverse(currentNode.left)
		self.traverse(currentNode.right)

	def remove(self,value):

		if self.root == None:
			return False

		currentNode = self.root
		print(f'currentNode {currentNode} self.root{self.root}')
		parentNode = None
		while(True):
			
			if parentNode != None:
				print(f'parentNode {parentNode.data}currentNode {currentNode.data} value {value}')
			if value < currentNode.data:
				currentNode = currentNode.left

			elif value > currentNode.data:
				currentNode = currentNode.right
			else:
				print('here')
				if currentNode.left != None:
					if parentNode.data < currentNode.data:
						parentNode.right = currentNode.left
					else:
						parentNode.right = currentNode.left
				elif currentNode.right != None:
					if parentNode.data < currentNode.data:
						parentNode.right = currentNode.right
					else:
						parentNode.right = currentNode.right

				else:
					if parentNode.data < currentNode.data:
						print(f'Deleting currentNode {currentNode}')
						parentNode.right = None
						currentNode = None
						del currentNode
					else:
						parentNode.right = None
					
				return True

			


		return False
					





bst1 = tree()

bst1.insert(9)
bst1.insert(4)
bst1.insert(20)
bst1.insert(15)
bst1.insert(130)
bst1.insert(100)
bst1.insert(6)

bst1.traverse(bst1.root)

bst1.remove(6)
# bst1.traverse(bst1.root)


print(bst1.search(9))