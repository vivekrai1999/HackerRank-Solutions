# solution notes
# pow(a,b) => takes two arguments a and b , returns the value of a raise to the power b, same as a**b
# if pow(a,b,z) => means a raise to the power b and modulud z 
# eg: pow(3,4,5) means 3 raise to the power 4 that is 81 and 81%5 that is 1
a = int(input())
b = int(input())
m = int(input())
print(pow(a,b))
print(pow(a,b,m))
