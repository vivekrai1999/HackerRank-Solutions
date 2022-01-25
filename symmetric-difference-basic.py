# solution notes 
# task: find the all elements that are not common in both the sets
# append appends object at the end.
# extend extends list by appending elements from the iterable.
_ = int(input())
set_m = set(map(int, input().split())) # getting first set input
_ = int(input())
set_n = set(map(int, input().split())) # getting second set input
s_difference1 = [] # crrating an array for storing the elements that are not common in both sets
s_difference1.extend(set_m.difference(set_n)) # .difference method gives the subtrsction of sets i.e. setA-setB gives all the elements that are only in setA all the common elements gets subtracted from set B
s_difference1.extend(set_n.difference(set_m)) # .difference method gives the subtrsction of sets i.e. setA-setB gives all the elements that are only in setB all the common elements gets subtracted from set A
for item in sorted(s_difference1): # printing all the elements in the s_difference1 list
    print(item)
