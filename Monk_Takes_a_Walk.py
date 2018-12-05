
'''

problem statement: https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/monk-takes-a-walk/

'''

def isVowels(chr):
    vowels = ['A', 'E', 'I', 'O', 'U' ,'a','e','i','o','u']
    if chr in vowels:
        return True
    else:
        return False

for t in range(int(input())):
    trees = list(map(isVowels,list(input())))
    print(trees.count(True))
