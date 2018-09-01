# Use stack to implement Reverse Polish notation
# Algorithm is quoted from wikipedia:
# for each token in the postfix expression:
#  if token is an operator:
#    operand_2 ← pop from the stack
#    operand_1 ← pop from the stack
#    result ← evaluate token with operand_1 and operand_2
#    push result back onto the stack
#  else if token is an operand:
#    push token onto the stack
# result ← pop from the stack

from stack import *
# Of course the py list functions are enough, just for practice

def rpn(expression):
	inputList = expression.split()
	# require the input tokens seperated by space
	stack0 = Stack()
	# initialize a stack to store temp results
	for token in inputList:
		if token == "+":
			operand2 = float(stack0.pop())
			operand1 = float(stack0.pop())
			result = operand1 + operand2
			stack0.push(result)
		elif token == "-":
			operand2 = float(stack0.pop())
			operand1 = float(stack0.pop())
			result = operand1 - operand2
			stack0.push(result)
		elif token == "*":
			operand2 = float(stack0.pop())
			operand1 = float(stack0.pop())
			result = operand1 * operand2
			stack0.push(result)
		elif token == "/":
			operand2 = float(stack0.pop())
			operand1 = float(stack0.pop())
			result = operand1 / operand2
			stack0.push(result)
		else:
			stack0.push(token)
	return(stack0.pop())

if __name__ == '__main__':
	print(rpn("3 4 +"))
	print(rpn("15 7 1 1 + - / 3 * 2 1 1 + + -"))