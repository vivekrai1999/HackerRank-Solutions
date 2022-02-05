# concatenate: Two or more arrays can be concatenated together using the concatenate function with a tuple of the arrays to be joined:
#              If an array has more than one dimension, it is possible to specify the axis along which multiple arrays are concatenated. By default, it is along the first dimension.
import numpy

list1 = []
list2 = []
n,m,p = map(int, input().split()) # getting row, column dimension
for _ in range(n): # getting inputs for n rows
    list1.append(list(map(int, input().split())))
for _ in range(m): # getting inputs for m rows
    list2.append(list(map(int, input().split())))

array1 = numpy.array(list1) # converting list to nummpy array
array2 = numpy.array(list2) # converting list to nummpy array

print(numpy.concatenate((array1, array2), axis = 0)) # concatenating numpy array 


