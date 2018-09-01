# This is the implementation of singly circular linked list (SC Linked List).
# Basic functions:
# initSCLinkedList() -- initialize an empty singly circular linked list
# insert(item) -- insert node
# remove(item) -- delte node
# search(item) -- check if in the list
# empty() -- check if list is empty
# size() -- count nodes in the list

class Node:
	def __init__(self, initdata):
		self.__data = initdata
		self.__next = None

	def getData(self):
		return self.__data

	def getNext(self):
		return self.__next

	def setData(self, newData):
		self.__data = newData

	def setNext(self, newNext):
		self.__next = newNext

class SCLinkedList:
	def __init__(self):
		self.head = Node(None)
		self.head.setNext(self.head)
		# head pointer points to itself at the beginning

	def insert(self, item):
		temp = Node(item)
		temp.setNext(self.head.getNext())
		# last item points to the head to form a circle
		self.head.setNext(temp)

	def remove(self, item):
		previous = self.head
		# start from head but cursor is at next to head
		flag = True
		while previous.getNext() != self.head:
			# loop until cursor meets head
			cursor = previous.getNext()
			# cursor is here
			if cursor.getData() == item:
				previous.setNext(cursor.getNext())
				flag = False
			previous = previous.getNext()
		if flag:
			print("Error!", item, "is not in this list.")

	def search(self, item):
		previous = self.head
		while previous.getNext() != self.head:
			cursor = previous.getNext()
			if cursor.getData() == item:
				return True
			previous = previous.getNext()
		return False
    # another style to implement remove and search:
    # cursor = self.head.getNext()
    # while cusor != self.head
    #     ...
    #     cursor = cursor.getNext()

	def empty(self):
		return self.head.getNext() == self.head
		# still remember the first homework of Haskell?

	def size(self):
		count = 0
		cursor = self.head.getNext()
		while cursor != self.head:
			count += 1
			cursor = cursor.getNext()
		return count

# Non-class functions
def printList(linkedList):
	# print the items in the list from the head
	cursor = linkedList.head.getNext()
	flag = True
	while cursor != linkedList.head:
		print("(",cursor.getData(),")", end = "-")
		flag = False
		cursor = cursor.getNext()
	if flag:
		print("This is an empty list.")
	print()

def join(list1, list2):
	# join two non-empty linked lists
	if (not list1.empty()) and (not list2.empty()):
		temp = list1.head.getNext()
		list1.head.setNext(list2.head.getNext())
		list2.head.setNext(temp)
		list2.head.setData("list2_head")
		list1.remove("list2_head")
		return list1

# test run
if __name__ == '__main__':
	list0 = SCLinkedList()
	print("List 0 has been initialized.")
	print("Is this list empty?", list0.empty())
	print("The size of this list is:", list0.size())
	printList(list0)
	print()

	list0.insert(1)
	print("insert item:", list0.head.getNext().getData())
	list0.insert("apple")
	print("insert item:", list0.head.getNext().getData())
	list0.insert("A")
	print("insert item:", list0.head.getNext().getData())
	printList(list0)
	print("Is this list empty?", list0.empty())
	print("The size of this list is:", list0.size())
	print()

	print("Is 100 in this list?", list0.search(100))
	print("Is apple in this list?", list0.search("apple"))
	print()

	list0.remove("apple")
	print("Item (apple) has been removed.")
	print("Is apple in this list?", list0.search("apple"))
	printList(list0)
	print("Is this list empty?", list0.empty())
	print("The size of this list is:", list0.size())
	print()

	print("Trying to remove apple again now.")
	list0.remove("apple")
	print()

	list1 = SCLinkedList()
	list2 = SCLinkedList()
	for i in range(11):
		list1.insert(i)
	for i in range(-1,-11,-1):
		list2.insert(i)
	print("List 1:")
	printList(list1)
	print("List 2:")
	printList(list2)
	print("Joined list:")
	printList(join(list1, list2))