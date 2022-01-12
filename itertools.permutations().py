# solution notes
# itertool.permutations() method provides us with all the possible arrangements that can be there for an iterator 
# permutations() takes two arguments 1. iterable(list/string/tuple/dictionary) 2. length of permutation needed
from itertools import permutations

S, k = input().split()
permutation = sorted(list(permutations(S, int(k)))) # getting permutation and sorting them
for item in permutation:
    print("".join(item)) # in permutation list joining all elements inside the item i.e. a tuple
