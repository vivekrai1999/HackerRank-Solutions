# solution notes:
# .swapcase() => swapes case of the string i.e. if the case is upper than it is converted to lower and vice versa
def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
