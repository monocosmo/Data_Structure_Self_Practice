# recursion
def revR(word):
	if len(word) <= 1:
		return word
	else:
		return revR(word[1:]) + word[0]
# iteration
def rev(word):
	result = []
	for letter in word:
		result.insert(0, letter)
	return ''.join(result)

if __name__ == '__main__':
	print(rev(''))
	print(rev('a'))
	print(rev('apple'))
	print(rev('1234567'))

	print(revR(''))
	print(revR('a'))
	print(revR('apple'))
	print(revR('1234567'))