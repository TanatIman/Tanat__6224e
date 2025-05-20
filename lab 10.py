import math
def f(x):
    return x*x-math.log(x+1)
def derivative_F(x):
    return 2*x+ (1/(x+1))
k=1
newk=0
while (abs(k-newk))>=0.001:
    newk=k-f(k)/derivative_F(k)
    k=newk-f(newk)/derivative_F(newk)
print (k)
