# solution notes
# getattr(A, operation)(elements) => SetA.update_difference(SetB)
number = int(input())
A = set(input().split())
N = int(input())
for _ in range(N):
    operation, length = input().split()
    elements = set(input().split())
    getattr(A, operation)(elements)
print(sum(list(map(int, A))))

