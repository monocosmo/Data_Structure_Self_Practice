# Implement stack with python list functions

class Stack(object):
	"""docstring for Stack"""
	def __init__(self):
		self.__stack = []

	def isEmpty(self):
		return self.__stack == []

	def top(self):
		if self.isEmpty():
			return False
		else:
			return self.__stack[-1]

	def size(self):
		return len(self.__stack)

	def push(self, item):
		self.__stack.append(item)

	def pop(self):
		return self.__stack.pop()

if __name__ == '__main__':
	stack0 = Stack()
	print("stack0 initialized.")
	print("Is stack0 empty?")
	print(stack0.isEmpty())
	print("Size of stack0:")
	print(stack0.size())
	if not stack0.top():
		print("Stack is empty, Top item unavailable")
	else:
		print(stack0.top())
	print()

	print("Push 1 to 10 into stack:")
	for i in range(1,11):
		stack0.push(i)
	print("Size of stack0:")
	print(stack0.size())
	print()

	print("Pop:")
	print(stack0.pop())
	print("Top item:")
	print(stack0.top())