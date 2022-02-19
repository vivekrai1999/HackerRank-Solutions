import re

n = int(input())
for _ in range(n):
    line = input()
    match = re.sub(r'(?<= )&&(?= )','and',line)
    print(re.sub(r'(?<= )\|\|(?= )','or', match))
