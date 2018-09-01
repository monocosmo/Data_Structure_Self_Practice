from stack import *
# Of course the py list functions are enough, just for practice

def inToPostfix(expression):
	inputList = expression.split()
	# require the input tokens seperated by space
	output = []
	stack0 = Stack()
	# initialize a stack to store temp results
	for token in inputList:
		if token == '+' or token == '-':
			if stack0.isEmpty() or stack0 == '(':
				stack0.push(token)
			else:
				while not stack0.isEmpty() and (stack0.top() == '*' or stack0.top() == '/'\
				or stack0.top() == '+' or stack0.top() == '-'):
					output.append(stack0.pop())
				stack0.push(token)
		elif token == '*' or token == '/':
			if stack0.isEmpty() or stack0.top() == '+' or stack0.top() == '-' or stack0 == '(':
				stack0.push(token)
			else: 
				while not stack0.isEmpty() and (stack0.top() == '*' or stack0.top() == '/'):
					output.append(stack0.pop())
				stack0.push(token)
		elif token == '(':
			stack0.push(token)
		elif token == ')':
			while stack0.top() != '(':
				output.append(stack0.pop())
			stack0.pop()
			# pop out '(' and discard
		else:
			output.append(token)
	while (not stack0.isEmpty()):
		# pop out the reset operators
		output.append(stack0.pop())
	return output

# test run
# a + b * c + ( d * e + f ) * g
if __name__ == '__main__':
	print (inToPostfix('a + b * c + ( d * e + f ) * g'))

import rpn
print(rpn.rpn(' '.join(inToPostfix('1 + 2 - 3 * 6 + ( 5 - 2 ) * 7 / 2 - 1'))))