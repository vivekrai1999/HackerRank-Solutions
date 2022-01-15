# Solution notes
# deque(): doubly ended queue
#          present in the collection module
#          prefered over list in case where we need quicker append and pop operations from both the ends of the container
#          list time complexity for append and pop : O(n)
#          deque time complexity for append and pop : O(1)
#          operations: append: append item to right end, appendleft: append item to left end, pop: pop item from right end, popleft: pop item from right end
# getter(object_name, string_value(output: object_name.string_value))(value for the function)
from collections import deque

N = int(input())
queue = deque() # creating object of deque() class
for _ in range(N): # running loop n times for n operations
    fun, *value = input().split() # getting two input, assigning forst value to the function and rest of the items to the values
    getattr(queue, fun)(*value) 
print(*queue) # printing all items of dqueue
