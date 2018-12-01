
'''

problem statement: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/range-query-2/

'''

def flip(lst, idx):
	lst[idx-1] = '0' if lst[idx-1] == '1' else '1'
	return lst

N, Q = map(int,input().split(' '))

number = input().split(' ')

for _ in range(Q):
	q = input().split(' ')

	if q[0] == '1':
		number = flip(number, int(q[1]))
	else:
		print('ODD') if number[int(q[-1])-1] == '1' else print('EVEN')
