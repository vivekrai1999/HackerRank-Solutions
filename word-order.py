# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
n = int(input()) # number of total word inputs
word = [] # list to store all the word inputs
count = [] # values recieved from dictionary in line 12 appends here
for _ in range(n): # running loop n times to get n inputs
    word.append(input()) # append each input to the word list
c = Counter(word) # count occurance of each word in the word list, it will return a dictionary with key= element in word list and value = number of times that element occures in the word list
word = set(word) # converting the word list to a set so that we can get the  number of dictinct elements(set only contains distinct elements)
print(len(word)) # by getting length of the set we can get the number of distinct elements
for key,value in c.items(): # iterating through each item in dictionary and apending the value in a seprate list, here value is the number of times the element is occuring in the list
    count.append(value)
print(*count) # print the all elements of count where each element denotes the number of occurance of each element in the list
 
