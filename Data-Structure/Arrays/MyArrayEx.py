class MyArray(object):

	def __init__(self):
		self.len = 0
		self.data = {}


	def push(self,item):

		self.data[self.len] = item
		self.len+=1

	def delete(self,index):

		if index > self.len -1 or self.data == {}:
			# print("Error !! Out of index")
			return None

		temp = self.data[index]
		del self.data[index]

		if index != self.len -1:
			self.shift_items(index)

		return temp

		

	def get_item(self,index):

		if index > self.len:
			return None
		else:
			return self.data[index]

	def shift_items(self,index):

		for i in range(index,self.len-1):
			self.data[i] = self.data[i+1]

		del self.data[self.len-1]
		
		self.len-=1

	def pop(self):

		#delete the first item:
		return self.delete(0)


arr = MyArray()

arr.push('A')
arr.push('B')
arr.push('C')
arr.push('D')
arr.push('E')

print(arr.__dict__)
print(arr.pop())
print(arr.__dict__)
print(arr.pop())
print(arr.__dict__)
print(arr.pop())
print(arr.__dict__)
print(arr.pop())
print(arr.__dict__)
print(arr.pop())
print(arr.__dict__)
print(arr.pop())
print(arr.__dict__)