# solution notes
# set is faster than list when it comes to searching operation.(provides better time complexity)
# list-comprehension:
# sum([(i in A) - (i in B) for i in array])
#       true    -   false  evaluates to 1
#       false   -   true   evaluates to -1
#       true    -   false  evaluates to 1
# final list = [1, -1, 1]
# sum of final list evaluates to 1

n, m = input().split()
array = input().split()
A = set(input().split())
B = set(input().split())
print(sum([(i in A)-(i in B) for i in array]))

# code with time error:
#
# n, m = input().split()
# array = map(int, input().split())
# A = map(int, input().split())
# B = map(int, input().split())
# count = 0
# for item in array:
#   if item in A:
#     count += 1
#   elif item in B:
#     count -= 1
# print(count)
