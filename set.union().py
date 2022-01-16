# solution notes
# set.union() => union operator returns union of set and a set of iterable.
# sometimes | operator is used in place of .union() operator
# Set is immutable to the .union() operation (or | operation). dosent changes the original set
n = int(input())
english = input().split() # getting roll numbers of students who take english newspaper
b = int(input())
french = input().split() # getting roll numbers of student who take french newspaper
print(len(set(english) | set(french))) # printing the length of union of both sets to get the student who take atleast one newspaper
