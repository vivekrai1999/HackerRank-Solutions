# solution notes - pending
from itertools import combinations
S, k = input().split()
S = sorted(S)
k = int(k)
data = []
for i in range(1,k+1):
    data.extend(list(combinations(S,i)))
for items in data:
    print("".join(items))
    
