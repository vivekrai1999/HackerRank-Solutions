# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
for _ in range(n):
    card = input()
    if re.findall(r'^[456][\d]{3}-{0,1}[\d]{4}-{0,1}[\d]{4}-{0,1}[\d]{4}$', card) and not re.findall(r'(\d)\1\1\1', card.replace('-','')):
        print('Valid')
    else:
        print('Invalid')
