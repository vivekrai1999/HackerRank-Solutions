# floor: The tool floor returns the floor of the input element-wise. nearest lowest integer
# ceil: The tool ceil returns the ceiling of the input element-wise. nearest greatest integer
# rint: The rint tool rounds to the nearest integer of input element-wise.

import numpy
numpy.set_printoptions(legacy='1.13')

arr = list(map(float, input().split()))
numarr = numpy.array(arr)
print(numpy.floor(numarr))
print(numpy.ceil(numarr))
print(numpy.rint(numarr))




