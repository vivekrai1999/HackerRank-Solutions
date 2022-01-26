# solution-notes
# counter is a method from collections module which counts occurance of each element in the list and returns a dictionary
from collections import Counter
k = int(input())
room_no = input().split() # list of room numbers
new = Counter(room_no) # generating a counter (dictionary with value and their occurance)
print(*[key for key,value in new.items() if value == 1]) # using dictionary comprehension to get the key whose value is equal to 1
