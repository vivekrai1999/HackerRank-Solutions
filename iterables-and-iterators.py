# solution notes pending
from itertools import combinations
n = int(input())
letters = input().split()
k = int(input())
counter = 0
combination = list(combinations(letters, k))
len_combination = len(combination)
for item in combination:
    if 'a' in item:
        counter += 1
print(counter/len_combination)

