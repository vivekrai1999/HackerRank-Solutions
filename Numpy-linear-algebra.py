import numpy

coff = list(map(float, input().split()))
x  = int(input())

print(numpy.polyval(coff, x))
