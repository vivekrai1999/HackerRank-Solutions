import string
alphabet = string.ascii_lowercase
l = []
def print_rangoli(size):
    for i in range(size):
        s = '-'.join(alphabet[i:n])
        l.append((s[::-1]+s[1:]).center(4*size-3,'-'))
    print('\n'.join(l[:0:-1]+l))
    
    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
