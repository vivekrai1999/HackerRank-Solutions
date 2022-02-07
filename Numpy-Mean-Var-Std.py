# mean: The mean tool computes the arithmetic mean along the specified axis.By default, the axis is None. Therefore, it computes the mean of the flattened array.
# var: The var tool computes the arithmetic variance along the specified axis.By default, the axis is None. Therefore, it computes the variance of the flattened array.
# std: The std tool computes the arithmetic standard deviation along the specified axis.By default, the axis is None. Therefore, it computes the standard deviation of the flattened array.
# round: The round() function returns a floating-point number rounded to the specified number of decimals. round(number, ndigits) 
# number - the number to be rounded
# ndigits (optional) - number up to which the given number is rounded; defaults to 0
import numpy

data = []

n, m = map(int, input().split())
for _ in range(n):
    data.append(list(map(int, input().split())))

numarr = numpy.array(data)
print(numpy.mean(numarr, axis=1))
print(numpy.var(numarr, axis=0))
print(round(numpy.std(numarr, axis=None), 11))
