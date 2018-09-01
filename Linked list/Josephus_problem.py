# Josephus problem implementation
# Problem description is quoted from Wikipedia, simplified.
# "People are standing in a circle waiting to be executed. 
# After two people are skipped, the next person is executed (#3, #6, #9 ...). 
# The procedure is repeated with the remaining people."

from circular_linked_list import *
# use circular liked list to mimic this problem

def josephus(n):
	if n >= 3:
	# start to run if the input is qualified
		list0 = SCLinkedList()
		for i in range(n, 0, -1):
		# generate a circular linked list with n items
		# Note: my insert methond is not append
			list0.insert(i)
			# the items are numbered from 1 to n
		print("Before executing:")
		printList(list0)
		cursor = list0.head
		remaining = n
		while remaining >= 3:
		# keep going until less than three items remaining
			count = 0
			while count < 3:
			# skip two items
				cursor = cursor.getNext()
				if cursor != list0.head and cursor.getData() != 0:
					count += 1
			cursor.setData(0)
			remaining -= 1
		print("After executing:")
		printList(list0)

# test run
if __name__ == '__main__':
	josephus(3)
	josephus(10)
	josephus(41)