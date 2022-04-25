
class HashMap(object):
	def __init__(self,size):
		self.hash_size = size
		self.data = [None] * self.hash_size 

	# hash function returns a address for the given key
	def _hash(self,key):

		hash_num = 0
		for i in range(len(key)):
			hash_num += i * ord(key[i]) 

		return hash_num % self.hash_size

	def insert(self,key,value):

		address = self._hash(key)

		if self.data[address] == None:
			self.data[address] = [[key,value]]
		else:
			self.data[address].append([key,value])


		
	def find(self,key):

		address = self._hash(key)

		# print(address)
		if self.data[address] != None:

			A = []
			for element in self.data[address]:
				if element[0] == key:
					A.append(element)
			return A
		else:
			return []

	def keys(self):

		key_arr = []
		for i in range(len(self.data)):

			if self.data[i] != None:
				# print(self.data[i])
				for j in range(len(self.data[i])):
					# print(self.data[i][j])
					if self.data[i][j][0] not in key_arr:
						key_arr.append(self.data[i][j][0])

		return key_arr


Player = HashMap(10)
Player.insert("Pritpal",35)
Player.insert("Pritpal",34)
Player.insert("Andy",34)
Player.insert("Andy",35)
print(Player.find("Pritpal"))
print(Player.find("Andy"))
print(Player.find("Andaa"))

print(Player.keys())


print(Player.data)


