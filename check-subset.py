# solution notes
# setA.issubset(SetB) returns true if A is a subset of B else it returns false.
T = int(input())
for _ in range(T):
    count_A = int(input())
    ele_A = set(map(int, input().split()))
    count_B = int(input())
    ele_B = set(map(int, input().split()))
    if ele_A.issubset(ele_B):
        print("True")
    else:
        print("False")
