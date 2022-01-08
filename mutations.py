# solution notes
# list is mutable and tuple is not mutable
# in order to make changes in tuple or string we have two methods:
# 1. convert the string or tuple into list and then chnage the character at given position and then convert it to string.
# 2. use slice function and string concatination.
def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
