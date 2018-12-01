
'''

problem statement: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/memorise-me/

'''
from sys import stdin, stdout  

N = int(stdin.readline())

numbers = stdin.readline().split()
#print(numbers)

countNumbers = {}

for num in numbers:
	if num not in countNumbers:
		countNumbers[num] = 1
	else:
		countNumbers[num] += 1

Q = int(stdin.readline())

#print(numDf)
for _ in range(Q):
	val = input()
	
	if val in countNumbers:
		print(countNumbers[val])
	else:
		print("NOT PRESENT")