# solution notes
# counter returns a dictionary with the element as key and element occurance as value
# 1. sort counter
# 2. use lambda x:-x[1] to sort the dictionary based on the second value in reverse order
# 3. further extend lambda with lambda x: (-x[1],x[0]) so it furthers sorts the list according to te first value where the second values are identical
from collections import Counter
if __name__ == '__main__':
    s = input()
    l = sorted(Counter(s).items(), key = lambda x:(-x[1],x[0]))[:3] ####-------MAGIC--------#### 
    for item in l:
        print(*item)
