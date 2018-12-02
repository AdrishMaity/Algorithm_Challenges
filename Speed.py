
'''

problem statement: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/speed-7/

'''
from sys import stdin

T = int(input())

for _ in range(T):
	cars = int(input())
	speeds = list(map(int,stdin.readline().split()))

	count = 1
	maxSpeed = speeds[0]
	for c in range(cars):
		if maxSpeed > speeds[c]:
			maxSpeed = speeds[c]
			count += 1

	print(count)