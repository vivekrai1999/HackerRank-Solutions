# zeros : The zeros tool returns a new array with a given shape and type filled with 0's
# ones : The ones tool returns a new array with a given shape and type filled with 1's
import numpy

dimension = tuple(map(int, input().split())) # getting array dimensions as single input and converting data to tuple
print(numpy.zeros(dimension, dtype = numpy.int)) # using tuple to give parameter to zeros abd converting the data type to int
print(numpy.ones(dimension, dtype = numpy.int)) # using tuple to give parameter to ones abd converting the data type to int
