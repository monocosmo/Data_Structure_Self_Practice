# Eight (or N) queens puzzle
# The problem of placing eight chess queens on an 8×8 chessboard,
# so that no two queens threaten each other.

# Reference 1: https://zhuanlan.zhihu.com/p/22846106
# Reference 2: https://en.wikipedia.org/wiki/Depth-first_search

import time
# Use time library to compare different solutions
n = 8
# Setup 8x8 chessboard
count1 = 0 # for sol1
count2 = 0 # for sol2
# Record the different possible combinations of queens position

# Solution 1
pos = [0] * n
# Use an array to record queen's position.
# e.g. value of pos[0] is 5 means on position (0,5) there is a queen
# (0, pos[0]) ~> (i, pos[i])
def sol1(row):
	# recursion starts from checking "row: 0, col: 0"
	global count1
	for col in range(n):
		# check conflict in each column
		flag = True
		for i in range(row):
			if col == pos[i] or col - pos[i] == row - i or col - pos[i] == i - row:
				flag = False
				break
		if not flag:
			continue
			# means skip the rest code, go to col + 1
		if row == n - 1:
			# cursor comes to the last row means all queens are ok
			count1 += 1
		else:
			pos[row] = col
			sol1(row + 1)
			# place this queen and continue the recursion

# Solution 2
# Use three arrays to record if there is one queen on each Y, Up or Down direction
Y = [False] * n
Up = [False] * (2 * n - 1)
Down = [False] * (2 * n - 1)
def sol2(row):
	global count2
	for col in range(n):
		j = row + col; k = n - 1 - row + col
		# record the current position on Up and Down direction
		if Y[col] or Up[j] or Down[k]:
			continue
		if row == n - 1:
			count2 += 1
		else:
			Y[col] = Up[j] = Down[k] = True
			sol2(row + 1)
			Y[col] = Up[j] = Down[k] = False

if __name__ == '__main__':
	print("Test run of Solution 1")
	tic = time.time()
	sol1(0)
	toc = time.time()
	print("Total possible combinations:", count1)
	print("Running time of Solution 1 is:", toc - tic)

	print("Test run of Solution 2")
	tic = time.time()
	sol2(0)
	toc = time.time()
	print("Total possible combinations:", count2)
	print("Running time of Solution 1 is:", toc - tic)