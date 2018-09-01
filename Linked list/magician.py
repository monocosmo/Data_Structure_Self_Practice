# Magician cards problem implementation
# Magician has a stack of 13 cards (1-13) in a certain order.
# He takes out the first one and turns around it. It is #1.
# Then he put #1 aside and takes the top two cards.
# The first one is put back to bottom of stack and turns around the second one.
# It is magically #2 ...
# He will finish the performance in this way.
# What is the original order of the stack.

from circular_linked_list import *
# use circular liked list to mimic this problem

def magician():
	list0 = SCLinkedList()
	for i in range(13):
		list0.insert(0)
	# initialize a stack with 13 items
	cursor = list0.head
	for card in range(1,14,1):
		count = 0
		while count < card:
			cursor = cursor.getNext()
			if cursor.getData() == 0:
				count += 1
		cursor.setData(card)
	return(list0)

# test run
if __name__ == '__main__':
	printList(magician())