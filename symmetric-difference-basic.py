# solution notes pending
_ = int(input())
set_m = set(map(int, input().split()))
_ = int(input())
set_n = set(map(int, input().split()))
s_difference1 = []
s_difference1.extend(set_m.difference(set_n))
s_difference1.extend(set_n.difference(set_m))
for item in sorted(s_difference1):
    print(item)
