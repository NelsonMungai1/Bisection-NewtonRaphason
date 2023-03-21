import math
from timeit import timeit
def f(x):
    return x**5+5*x**4-2
def df(x):
    return 5*x**4+20*x**3



tolerance=1e-6
max_iterations=1000
# to be able to find the intelligent guess
import matplotlib.pyplot as plt
import numpy as np
x=np.array(range(-20,20))
print(x)
y=x**5+5*x**4-2
print(y)
plt.plot(x,y)


def newRaphason():
    x0=1
    for i in range(max_iterations):
        fx=f(x0)
        dfx=df(x0)
        x1=x0-(fx/dfx)
        print(f'no of iteration {i}')
        if abs(f(x1))<tolerance:
            print(f'Root of the function is:{x1}')
            print(f'Time taken to run the program:')
            print(+timeit())
            break
        else:
            x0=x1

newRaphason()

def bisection():
    a=0
    b=3
    for i in range(max_iterations):
        c=(a+b)/2
        print(f'Iteration number: {i}')
        if abs(f(c))<tolerance:
            print(f'Found root at {c:.6}')
            print("Time taken for bisection method")
            print(timeit())
            break
        elif f(c)*f(b)<0:
            a=c
        else:
            b=c

bisection()
