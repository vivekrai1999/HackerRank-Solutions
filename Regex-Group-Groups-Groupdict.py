import re
s = input()
match = re.findall(r'([a-zA-Z0-9])\1+',s)
if bool(match):
    print(match[0])
else:
    print(-1)
