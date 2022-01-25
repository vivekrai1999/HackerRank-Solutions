# solution notes 
# zip() function: This function returns a list of tuples. The th tuple contains the th element from each of the argument sequences or iterables.
# If the argument sequences are of unequal lengths, then the returned list is truncated to the length of the shortest argument sequence.
N, X = map(int, input().split())
data = []
for _ in range(X):
    data.append(list(map(float, input().split()))) # getting marks of student in each subject, making it a list and appending it to another list called data.
for item in list(zip(*data)): # *data will give all the iterators inside the data list to the zip function and zip function will return list of tuples. so this line can be interpreted as for each item in the returned list i.e. for each tuple get the sum of while tuple and divide it with the length of the tuple to get average.
    print(sum(item)/len(item))
