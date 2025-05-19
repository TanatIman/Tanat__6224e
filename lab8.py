import math
def f(x):
    return x*x-math.log(x+1)
def bisection(a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
      print ("No root in this interval")
    for i in range(max_iter):
        c = (a + b) / 2
        if abs(f(c)) < tol or (b - a) / 2 < tol:
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2
root = bisection(0.1,0.9)
print (f"the root is : {root}")