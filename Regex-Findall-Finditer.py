# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s = input()

match = re.findall(r'([AEIOUaeiou]{2,})[BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz]', s)
if match:
    for i in match:
        print(i)
else:
    print(-1)
