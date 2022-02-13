import re
t = int(input())
for _ in range(t):
    data = input()
    print(bool(re.match('^[-+]?[0-9]*\.[0-9]+$', data)))
