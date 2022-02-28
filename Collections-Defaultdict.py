from collections import defaultdict

n, m = input().split()
a = defaultdict(list)
b = []
match = []
match_found = False
for i in range(int(n)):
    a[i].append(input())
for j in range(int(m)):
    b.append(input())
for item in b:
    for element in a.items():
        if [item] == element[1]:
            match.append(element[0]+1)
            match_found = True
    if match_found == False:
        match.append(-1)
    print(*match)
    match_found = False
    match.clear()
