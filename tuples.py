# solution notes
# .split() => gets a string and creates a list with all items of string
# map() => takes an iterable and performs an action on each element of the iterable
# tuple(integer_list) => type casting the list to a tuple
# Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.(TO BE STUDIED)
if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    t = tuple(integer_list)
    print(hash(t))
        
