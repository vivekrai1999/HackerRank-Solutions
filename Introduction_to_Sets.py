# solution notes
# set() method takes an iterable and returns a list of distinct items.
# in order to find average sum all the distinct values obtained from set method and then divide the value with the length of the list obtained from set method

def average(array):
    return sum(set(array))/len(set(array))
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
