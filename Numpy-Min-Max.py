# min:The tool min returns the minimum value along a given axis.By default, the axis value is None. Therefore, it finds the minimum over all the dimensions of the input array.
# max: The tool max returns the maximum value along a given axis.By default, the axis value is None. Therefore, it finds the maximum over all the dimensions of the input array.


import numpy

data = []

n, m = map(int, input().split())
for _ in range(n):
    data.append(list(map(int, input().split())))
    
numarr = numpy.array(data)
min_along_1 = numpy.min(numarr, axis=1)
print(numpy.max(min_along_1))
