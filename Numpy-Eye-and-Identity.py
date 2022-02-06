# identity : The identity tool returns an identity array. An identity array is a square matrix with all the main diagonal elements as 1 and the rest as 0. The default type of elements is float.
# eye: The eye tool returns a 2-D array with 1's as the diagonal and 0's elsewhere. The diagonal can be main, upper or lower depending on the optional parameter . A positive k is for the upper diagonal, a negative k is for the lower, and a   0 k (default) is for the main diagonal.
import numpy
numpy.set_printoptions(legacy='1.13')

n, m = map(int, input().split()) # taking n and m , here n = number of rows and m = number of columns
print(numpy.eye(n, m))


