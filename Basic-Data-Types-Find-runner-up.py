# solution using list comprehension
# max() gives the greatest element in a list
# split() is used to convert a string into a list
# map() is used to perform an action on each element of the list e.g. here we are converting the string into int elements.
# logic: 1. find the first maximum number
#        2. delete all occurance of the maximum number
#        3. again find the maximum number in the list
#        4. now we get the second runner up
# solution 1
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    new_list = [item for item in arr if item != max(arr)]
    print(max(new_list))

# solution 2 - 21 feb 2022
if __name__ == '__main__':
    _ = int(input())
    sort_array = sorted(map(int, input().split()))
    print([i for i in sort_array if i != sort_array[-1]][-1])
