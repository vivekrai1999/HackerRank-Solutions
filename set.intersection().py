# solution notes
# set.intersection() => returns the intersection of a set and a set of elements in list.
# the set is immutable to the .intersection() or & operation.
n = int(input())
english = input().split()
b = int(input())
french = input().split()
print(len(set(english) & set(french))) # getting length of intersection of two sets
