
'''

problem statement: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/maximize-the-earning-137963bc-323025a6/

'''

from sys import stdin

noOfStreet = int(stdin.readline())

for _ in range(noOfStreet):
	N,R = map(int, stdin.readline().split())

	heights = stdin.readline().split()

	count = 0
	tempHeight = 0
	for h in heights:
		if tempHeight < int(h):
			count += 1
			tempHeight = int(h)
	print(count*R)

