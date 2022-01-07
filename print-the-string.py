#solution 1
if __name__ == '__main__':
    n = int(input())
    data = []
    for i in range(1, n+1)
      data.append(str(i))
    print("".join(data))

# solution 2
# using map and join function
# map: takes two arguments 1. function 2. iterable
# iterable can be any list,tuple,range etc.
# function is any action that is to be applied in each of the item in iterable.
# map returns a map object which is also an iterable

if __name__ == '__main__':
    n = int(input())
    print("".join(map(str, range(1, n+1))))
