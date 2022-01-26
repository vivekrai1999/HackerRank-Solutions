# solution notes
# task: we are given a set a and N number of other sets, we  need to check if a is strict superset of all the n sets.
# if a is strict superset of all the n sets then print true else print false
# strict superset: A strict superset has at least one element that does not exist in its subset.
# required conditions for strict superset: 
# 1. b needs to be the subset of a.
# 2. there must be elements in a that does not exist in b we can check this by subtracting set b from set a so we get all the values that are not in set b.

a = set(input().split()) # getting set a
boolean = [] # for storing boolean result of each check
for _ in range(int(input())): # running loops n times for n sets
    b = set(input().split()) # getting set b
    if b.issubset(a) and len(a.difference(b)) > 0: # if b is a subset of a and the difference of a-b has elements in it then we can say a is a strict superset of b
        boolean.append(True) # if condition gets true then append true to the boolean list
    else:
        boolean.append(False)  # else append false to the boolean list
print(all(boolean))  # finally use all on iterable boolean so if all the values of the iterable are true it will return true.
