
'''

problem statement: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/monk-and-welcome-problem/

'''

N = int(input())
A = list(map(int,input().split(' ')))
B = list(map(int,input().split(' ')))

print(" ".join(map(str,[a+b for a,b in zip(A,B)])))