# Fibonacci array

# recursion version
def fab(max):
	result = []
	n, a, b = 0, 0, 1
	while n < max:
		result.append(b)
		a, b = b, a + b
		n = n + 1
	return result

# generator version
def fabG(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a + b
		n = n + 1

if __name__ == '__main__':
	print(fab(5))
	for n in fab(5):
		print(n)
