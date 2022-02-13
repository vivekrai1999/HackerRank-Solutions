import re

n = int(input())
for _ in range(n):
    x, y = input().split()
    m = bool(re.match(r"<[a-zA-Z][\w.-]+@[a-zA-Z]+\.[a-z]{1,3}>", y))
    if m:
        print(x,y)

