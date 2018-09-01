# recursion
def factorialR(n):
	if n == 1:
		return 1
	else:
		return n*factorialR(n-1)

# tail recursion
def factorialT(n, acc = 1):
	# remeber acc in Haskell fold?
	if n == 1:
		return acc
	else:
		return factorialT(n-1, n*acc)

# iteration
def factorialF(n):
	result = 1
	while n > 1:
		result = result * n
		n -= 1
	return result


if __name__ == '__main__':
	print(factorialR(1), end = ",")
	print(factorialR(2), end = ",")
	print(factorialR(3), end = ",")
	print(factorialR(4), end = ",")
	print(factorialR(5))

	print(factorialF(1), end = ",")
	print(factorialF(2), end = ",")
	print(factorialF(3), end = ",")
	print(factorialF(4), end = ",")
	print(factorialF(5))

	print(factorialT(1), end = ",")
	print(factorialT(2), end = ",")
	print(factorialT(3), end = ",")
	print(factorialT(4), end = ",")
	print(factorialT(5))