# solution notes
# fractions module => it deals with rational number arithmetic.
#                     it alows to create a function instance from integers, floats, decimals, strings.
# fraction instances: a fraction instance can be constructed from a pair of integers, from another rational number or from a string.
#                     fraction instances are hashable and should be treated as immutable
# creating fraction instance => fractions.Fraction(numerator = , denominator = )
# example: Fraction(2, 3) gives output as 2/3
#
# reduce function: reduce(function, sequesncce) is used to apply a particular function, that is passed in it to all the list elements mentioned in the sequence passed along
# reduce function is defined in functools module.
# working: 
#1. at first two elements of the sequence are picked and the result is obtained.
# 2. in next step apply the same function to the previously attained result and the number just succedding the second element an dthe result is again stored.
# 3. the process continues till no elements are left in the container.
# 4. the final result is returned and printed on the console.
# application:  reduce(function, sequence, initializer)
# example: reduce(lambda a,b: a+b, [1,2,3])
# output: 6
from fractions import Fraction
from functools import reduce

def product(fracs):
    t = reduce(lambda x,y: x*y , fracs) # using reduce multiply each rational number
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split()))) # example: Fraction(2,3) and then it append to fracs list
    result = product(fracs)
    print(*result)
