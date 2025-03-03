import math
S=0
x=0.2
n=1
while abs((math.sin(x**n))/n)>=0.01:
    if n%2==1:
        S+=(math.sin(x**n)/n)
    else:
        S-=(math.sin(x**n)/n)
    n+=1
print(S)