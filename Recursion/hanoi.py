# use recursion to implement Hanoi
def hanoi(n, a, b, c):
	# a, b, c are three poles. c is destination.
	if n == 1:
		print(a, "->", c, end = "; ")
	# recursion boundary
	else:
		hanoi(n-1, a, c, b)
		# top n-1 blocks will be put in b (buffer) temporarily
		hanoi(1, a, b, c)
		# move the last one from a to c directly
		hanoi(n-1, b, a, c)
		# a is empty now, so serves as buffer to transfer blocks from b to c

if __name__ == '__main__':
	hanoi(1, "a", "b", "c")
	print()
	hanoi(2, "a", "b", "c")
	print()
	hanoi(5, "a", "b", "c")