import numpy as num

elements = list(map(int, input().split())) # getting single line input
my_array = num.array(elements) # creating an numpy array with list
my_array.shape = (3,3) # using shape to convert the array to desired shape
print(my_array) # printing new shaped array
