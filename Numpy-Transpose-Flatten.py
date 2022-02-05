# transpose: We can generate the transposition of an array using the tool numpy.transpose. It will not affect the original array, but it will create a new array.
# flatten: The tool flatten creates a copy of the input array flattened to one dimension.
import numpy

data = []
n, m = map(int, input().split()) # getting row, column size
for _ in range(n): # getting data for n rows
    data.append(list(map(int, input().split()))) # appending each row elements in a data list as a nested list
my_array = numpy.array(data) # converting data list to numpy array
print(numpy.transpose(my_array)) # getting transpose of the numpy array
print(my_array.flatten()) # getting flatten of the numpy array
