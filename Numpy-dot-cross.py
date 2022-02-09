import numpy

data1 = []
data2 = []

n = int(input())
for _ in range(n):
    data1.append(list(map(int, input().split())))

for _ in range(n):
    data2.append(list(map(int, input().split())))
    
a = numpy.array(data1)
b = numpy.array(data2)

print(numpy.dot(a, b ))
