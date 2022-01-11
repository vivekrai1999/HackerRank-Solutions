# solution notes
# string.center(width, character) => centers a string, takes two arguments width(eg if width = 8 then then it spaces out the string from left and right), character(if space is not needed we can replace space with caharacter of our choice)
# module 1 : printing the top portion of the mat, running loop n//2 times to print vertically and centering the shape while printing it x times, initial value of x is 1 which increment as 1,3,5,7... so we increase value of x by adding common difference 2
# module 2 : print the center string
# from module 1 value of x is 7
# so now we have to print x in decreasing order, so if the initial value of x is 7 then we will print shape x-2 times and further decrement x by 2
n, m = input().split()
center_text = "WELCOME"
shape = '.|.'
x = 1
for i in range(int(n)//2):
    print((shape*x).center(int(m), "-"))
    x += 2
print(center_text.center(int(m), "-"))

for i in range(int(n)//2):
    print((shape*(x-2)).center(int(m), "-"))
    x -= 2
