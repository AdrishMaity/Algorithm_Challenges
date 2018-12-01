'''

problem statement: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/micro-and-array-update/

'''


numOfTestCases = int(input())

for testCase in range(numOfTestCases):
	N,K = map(int,input().split(' '))
	
	minimumNumberInList = min(map(int,input().split(' ')))
			
	timeCounter = 0
	
	if K > minimumNumberInList:
		timeCounter = K - minimumNumberInList
	
	print(timeCounter)