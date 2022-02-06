# sum: The sum tool returns the sum of array elements over a given axis. By default, the axis value is None. Therefore, it performs a sum over all the dimensions of the input array.
# product: The prod tool returns the product of array elements over a given axis. By default, the axis value is None. Therefore, it performs the product over all the dimensions of the input array.


import numpy

data = []

n, m = map(int, input().split())
for _ in range(n):
    data.append(list(map(int, input().split())))

numarr = numpy.array(data, int)
arrsum = numpy.sum(numarr, axis=0)
print(numpy.product(arrsum))
