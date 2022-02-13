# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n = int(input())
for i in range(n):
    number = input()
    if re.match(r'^[789][0123456789]{9}$', number):
        print("YES")
    else:
        print("NO")
