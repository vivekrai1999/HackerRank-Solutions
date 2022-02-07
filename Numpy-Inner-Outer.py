# inner:The inner tool returns the inner product of two arrays.
# outer: The outer tool returns the outer product of two arrays.
import numpy

a = numpy.array(list(map(int, input().split())))
b = numpy.array(list(map(int, input().split())))
print(numpy.inner(a,b))
print(numpy.outer(a,b))
