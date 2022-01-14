# solution notes
# ordereddict is available in collection module
# .rpartition(): splits a given string into three parts
#                starts looking for seprator from right side
#                return a tuple which contains part of the string before separator, argument of the string and the part after the separator.
# .get(keyname, value(A value to return if the specified key does not exist.)): The get() method returns the value of the item with the specified key.
# logic: assign dicto[item_name] = price + if they key exist in the dicto dictionary already then its value i.e. the price else it returns 0 if the key disent exist in dictionary

from collections import OrderedDict
N = int(input())
dicto = OrderedDict()
for i in range(N):
    item_name, space, price = input().rpartition(' ')
    dicto[item_name] = dicto.get(item_name, 0) + int(price)
for key, value in dicto.items(): # for each key and value in dicto.items() print key and value
    print(key,value)
        
