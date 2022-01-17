# solution notes
# setA.difference(setB) or A - B : returns a set with all the elements in a set but not in the iterable.
#                        sometimes - operator is used in place of the .difference operator
#                        sets are immutable to the .difference or - operations
n_eng, r_eng = int(input()), input().split()
n_french, r_french = int(input()), input().split()
print(len(set(r_eng)-set(r_french))) # using - operation in place of .difference operation
print(len(set(r_eng).difference(r_french))) # using .difference() opeartion
