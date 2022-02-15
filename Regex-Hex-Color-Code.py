# (?<!^) : this syntax is known as negative lookbehind which ensures (?<=!B)A there occurs no B before A. in our case our expression evaluates as there is no starting of the line before our hex color code
#          so the id in css will not be evaluated as the hex color code because before id there is starting of the line.
# (?:[a-fA-F0-9]{3}) , (?:) indicates that the subpattern -- [a-fA-F0-9]{3} -- is a non capture subpattern. meaning whatever is matched in the (?:[a-fA-F0-9]{3}) even though it is enclosed by () it wont appear in the list of matches
# it prevents capturing of subgroups for example in #ff8ffa it will not capture #ff8(subpattren of #ff8ffa)
import re

n = int(input())
for _ in range(n):
    i = input()
    match = re.compile(r"(?<!^)#((?:[a-fA-F0-9]{3}){1,2})")
    m = match.findall(i)
    if m:
        for item in m:
            print(f'#{item}')
    
    

