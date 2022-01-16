# solution notes
# divmod(a,b) => take stwo arguments a and b and returns a tuple with quotient followed by remainder
# eg: a = 117
#     b = 10
#     divmod(a,b) gives (17, 1)
a = int(input())
b = int(input())
print(a//b) # integer division
print(a%b) # modulo givers remainder
print(divmod(a,b)) # returns tuple with quotient and remainder
