"""
Given following pattern write a function print(int n):
n=1 : 1
n=2 : 2 1 2
n=3 : 3 2 3 1 2 3
n=4 : 4 3 4 2 3 4 1 2 3 4
"""

def printN(n):
	level = n
	while level > 0:
		print(' '.join([str(i) for i in range(level, n+1)]), end = ' ')
		level -= 1
	print()


if __name__ == '__main__':
	printN(1)
	printN(2)
	printN(3)
	printN(4)