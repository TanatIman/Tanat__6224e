z=list()
b=int(input("b:"))
a=2
while a<=4:
    if b**2-2*a**2<=2.5:
        z.append(7*a**2+b)
    else:
        z.append(3*b-a)
    a+=0.5
print(z)
print(z[-1])
        