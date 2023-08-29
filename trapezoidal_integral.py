import math

a=0
b=1
n=100

def trapezoidal_integration(func, a, b, n):
    h = (b - a) / n
    integral = 0.0

    for i in range(n+1):
        x = a + i * h
        if i == 0 or i == n:
            integral += func(x)
        else:
            integral += 2 * func(x)
    
    integral *= h / 2
    return integral
#(1)
def f(x):
    return math.sin(x)

a = 0  
b = math.pi/2  
n = 50  

result = trapezoidal_integration(f, a, b, n)
print("積分結果:", result)

#(2)
def f(x):
    return 4/(1+x**2)

a = 0  
b = 1
n = 100  

result = trapezoidal_integration(f, a, b, n)
print("積分結果:", result)

#(3)
import math

def f(x):
    return math.pi**(1/2)*math.exp(-(x**2))
a=-100
b=100
n=1000

result = trapezoidal_integration(f, a, b, n)
print("積分結果:", result)