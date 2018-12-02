
'''

problem statement: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/b-39/

'''

from bisect import bisect_right
from sys import stdin

N = int(stdin.readline())

A = list(map(int,stdin.readline().split()))
B = list(map(int,stdin.readline().split()))

count = 0

B.sort()

z=1
for ai in A[1:]:
    k=0
    for aj in A[:z]:
        if ai>aj:
            k+=1
    count+=(N-bisect_right(B,ai))*k
    z+=1
print(count)