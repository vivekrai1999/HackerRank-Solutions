# solution notes
# collections: A module
# counter: class in collections module
#          it is a container that holds objects like list tuple and dictionary
#          sub class of dictionary
#          returns a dictionry with element and their respective count

from collections import Counter

X = int(input()) # number of shoes
shoes = Counter(map(int, input().split())) # returns a dictionary with shoes size with their respective counts
N = int(input()) # number of customers

income = 0 # final income counter

for i in range(N): # run loop for each customer
    shoes_size, price = map(int, input().split()) # take input for each customer's shoes size and price paid
    if shoes[shoes_size]: # if shoes size available in shoes dictionary in line 11 then increase the income counter by the price of the shoes paid 
        income += price # then increase the income counter by the price of the shoes paid 
        shoes[shoes_size] -= 1 # in shoes dictionary at line 11 using the dictionary key decrement the respective count by 1(when the respective count become 0 then when if bloack checks the condition shoes_size then the if condition wont run so no increment in income counter)
print(income)
