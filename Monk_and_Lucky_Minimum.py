
'''

problem statement: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/monk-and-lucky-minimum-3/

'''

from sys import stdin

T = int(input())

for _ in range(T):
	N = int(input())
	A = list(map(int,stdin.readline().split()))

	print("Lucky") if A.count(min(A)) % 2 == 1 else print("Unlucky")
