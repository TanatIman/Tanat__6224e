import math
def f(x):
    return math.sqrt(math.log(x+1))
epslon=0.001
k=1
newk=0
while (abs(k-newk)) >=0.001:
    newk=f(k)
    k=f(newk)
print (k)