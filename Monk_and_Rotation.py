
'''

problem statement: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/monk-and-rotation-3/

'''

from sys import stdin
from collections import deque

T = int(input())

for _ in range(T):
	N, K = map(int,stdin.readline().split())

	A = deque(map(int,stdin.readline().split()))
	#print(A)
	A.rotate(K)
	#print(list())
	print(' '.join(map(str,list(A))))