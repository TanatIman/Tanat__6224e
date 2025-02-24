import math
s=1/3**(0.2073)*math.sin(4)-(35/19)*math.cos(1)
t=(math.tan(2))*((math.e)**2)
if s<=t:
    m=3*abs(s*t)
else:
    m=s+t
print(m)