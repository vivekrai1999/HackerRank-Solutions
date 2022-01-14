# solution notes:
# .add() : this method adds a given element to a set if the element is not present in the set.
# add() method dosen't adds the element to the set if it is already present in it, otherwise it will get added to the set.
# .add() takes single parameter(element) which needs to be added in the set
N = int(input()) # number of total stamps
country = set() # initializing empty set
for i in range(N): # getting country of each stamp
    country.add(input()) # using add() method to add elements in the set. note: it will only add elements which are not present in the set already
print(len(country)) # print the length of the list to get count of distinct country stamps
    
    
