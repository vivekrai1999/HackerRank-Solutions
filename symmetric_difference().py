# solution notes
# setA.symmetric_difference(setB): returns a set with all the elements that are in the set and the iterable but not both.\
#                                  sometimes ^ operator is used in place of the .symmetric_difference() operator
#                                  a set is immutable to .symmetric_difference() or ^ operations.
n_eng = int(input())
r_eng = input().split()
n_french = int(input())
r_french = input().split()
# print(len(set(r_eng) ^ set(r_french))) # ^ operator can be used in place of .symmetric_difference() operator
print(len(set(r_eng).symmetric_difference(set(r_french)))) # getting length of output of symmetric_difference()
