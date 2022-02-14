import re
t = int(input())
pattern = re.compile(r"[A-Za-z0-9]{10}")
pattern1 = re.compile(r"[A-Z]")
pattern2 = re.compile(r"[0-9]")
for _ in range(t):
    uids = input()
    if len(list(uids)) != len(set(uids)):
        print('Invalid')
    else:
        if re.fullmatch(pattern, uids):
            if len(re.findall(pattern1,uids)) >= 2:
                if len(re.findall(pattern2, uids)) >= 3:
                    print('Valid')
                else:
                    print('Invalid')
            else:
                print('Invalid')
        else:
            print('Invalid')     
