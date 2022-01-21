# solution notes pending
N, X = map(int, input().split())
data = []
for _ in range(X):
    data.append(list(map(float, input().split())))
for item in list(zip(*data)):
    print(sum(item)/len(item))
