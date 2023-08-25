from math import sin
from math import pi
# --example--
# print(sin(0))
# >>> 0
# -----------
k=1
T=0
while k<=100:
    h=pi/(2*100)
    s=(h/2)*(sin((k-1)*h)+sin(k*h))
    T+=s
    k+=1
print(T)