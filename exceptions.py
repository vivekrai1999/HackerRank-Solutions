# error Handeling:
# syntax: try:
#           code
#         except error name
#            print something

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input()) #test for multiple inputs


for _ in range(n): # loop for taking multiple inputs
    a,b = input().split()  #getting new input each time the for loop runs
    try:
        print (int(a) // int(b))
    except ZeroDivisionError as e:
        print ("Error Code:",e)
    except ValueError as v:
        print ("Error Code:",v)
        
    
