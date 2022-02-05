# array: A NumPy array is a grid of values. They are similar to lists, except that every element of an array must be the same type.
import numpy

def arrays(arr):
    arr.reverse() # reverse the list
    my_array = numpy.array(arr, float) # creating numpy array of float dtype from python list
    return my_array 

arr = input().strip().split(' ') # getting single line input and storing them into list
result = arrays(arr) # passing list to arrays function
print(result)
