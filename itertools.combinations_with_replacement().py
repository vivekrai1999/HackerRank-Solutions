# Solution notes
# combinations_with_replacement(iterable, r) : 
# 1. it returns a 'r' length subsequence from the input iterable, allowing individual elements to be repeted more than once.
# 2. combinations are emitted in lexicographical sorted order.
# 3. if the input is sorted the resultant tuple will be in sorted order.
from itertools import combinations_with_replacement
S, k = input().split()
combination_list = list(combinations_with_replacement(sorted(S), int(k))) # sorting the input to get the desired sorted output, converting input k to  int
for item in combination_list: # for each item in the list we join the item and print
    print("".join(item))
