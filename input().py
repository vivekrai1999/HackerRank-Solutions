# solution notes
# eval(expression) => evaluates the expression and returns the result.
# here p = x**3 + x**2 + x + 1
x, k = map(int, input().split())
p = input()
if eval(p) == k:
    print("True")
else:
    print("False")
