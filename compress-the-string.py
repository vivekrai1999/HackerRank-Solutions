# solution notes
from itertools import groupby
S = input()
data = []
for key, group in groupby(S):
    tuple1 = (len(list(group)), int(key))
    data.append(tuple1)
print(*data)
    
