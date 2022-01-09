# better approch
# any() => checks if any of the items in a list is true and returns true if there is atleast one true
# [char.isalnum() for char in s] => list comprehension that appends true of false to the list while checking python string validator methods.

if __name__ == '__main__':
    s = input()
    print (any([char.isalnum() for char in s]))
    print (any([char.isalpha() for char in s]))
    print (any([char.isdigit() for char in s]))
    print (any([char.islower() for char in s]))
    print (any([char.isupper() for char in s]))


# solution 1(self)
# notes:
# .isalnum() => checks if all characters of string are alphanumeric
# .isalpha => check if all the character of a string are alphabets
# .isdigit() => check is all the characters of a string are digits
# .islower() => check if all the characters of a string has lowercase
# .isupper() => check if all the characters of string has uppercase

# setting initial flag values to false
# we are running for loop to test each case
# if any of the character in string matches the case then we set the flag value to true, and this flag value further cannot be modified

# problems i faced:
# if i run a single for loop and test all the cases with multiple if statement then there will be more print statement, i.e. for each character check 3 print statement and for 5 checks there will be total 15 print statements.
alnum = False
alpha = False
digit = False
lower = False
upper = False

if __name__ == '__main__':
    s = input()
    for letter in s:
        if letter.isalnum():
            alnum = True
    for letter in s:
        if letter.isalpha():
            alpha = True
    for letter in s:
        if letter.isdigit():
            digit = True
    for letter in s:
        if letter.islower():
            lower = True
    for letter in s:
        if letter.isupper():
            upper = True
    print(alnum)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)
