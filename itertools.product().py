# solution notes
# This tool computes the cartesian product of input iterables.
# It is equivalent to nested for-loops.
# For example, product(A, B) returns the same as ((x,y) for x in A for y in B).
# product(A, B) => computes cartesian product of input iterables

from itertools import product
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(*product(A, B)) # print all items of result product(A,B)

