# solution notes:
# run a loop in range 0 to length of the string
# using .find(string_to_find, start_index) get the index of first occurance of substring.
# if the .find() method doesnt find the substring then itll return -1. so in that case we'll break the loop.
# create a new list to store occurance of the substring in main string i.e. new list will contain index of each occurance then we will count the length of the list and we will get the total number of occurance of substring in a given string
# if find method returns a index then from next iteration start from the (index returned by the find method + 1)

def count_substring(string, sub_string):
    start = 0
    occurance = []
    for _ in range(0,len(string)):
        index = string.find(sub_string, start)
        if index == -1:
            break
        occurance.append(index)
        start = index+1
    return len(occurance)
    

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
