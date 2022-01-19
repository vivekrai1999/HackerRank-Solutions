# solution notes
# problem faced: we are taking two inputs in a single line 1. command, 2. value but with pop we are only passing the pop command with no value so the split gives the value error: expected two got 1
# solution: so we use *value so the remaining input after the first goes into value list.
#            then we convert each item of tyhe value list to integers
#             then we use getattr command and pass value to set s with command and *value i.e. the items of the list, in case of pop operation blank is there in list so pop gets no values
# after performing all the operations N times we generatethe sum of elements of set by sum method

n = int(input())
s = set(map(int, input().split()))
for _ in range(int(input())):
    command, *value = input().split()
    value = list(map(int, value))
    getattr(s, command)(*value)
print(sum(s))
