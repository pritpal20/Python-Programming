import sys
import linkedlist 

def main(argv):

	mylist = linkedlist.list('D')

	for i in range(1,10):
		mylist.append(i)
	
	print(mylist.len())
	print( mylist.display())

	mylist.insert(0,'A')
	mylist.insert(1,'B')

	print(mylist.display())
	print(mylist.len())


	mylist.print()

	print(mylist.__dict__)
	
	mylist.erase(1)
	mylist.erase(1)
	mylist.erase(0)
	mylist.print()
	print(mylist.len())



if __name__ == '__main__':

	main(sys.argv)