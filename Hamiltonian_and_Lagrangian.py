
'''

problem statement: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/hamiltonian-and-lagrangian/

'''

from sys import stdin

n = int(stdin.readline())

numbers = list(map(int,stdin.readline().split()))
newList = str(numbers[-1])
curMax = numbers[-1]
for i in range(n-2,-1,-1):

	if numbers[i] >= curMax:
		newList = str(numbers[i]) + ' ' + newList
		curMax = numbers[i]
print(newList)