import numpy as np
from math import cos, cosh, sin, sinh, tan, ceil, log, exp, pi

def f1(x):
    return cos(x)*cosh(x) - 1

def f2(x):
    return 1/x - tan(x)

def f3(x):
    return 2**(-x) + exp(x) + 2*cos(x) - 6

def bisection(a, b, func, eps, abs_err):
    n = ceil(log((b-a)/eps)/log(2))
    for i in range(n):
        mid = a + (b-a)/2
        f_mid = func(mid)

        if np.sign(func(a)) != np.sign(f_mid):
            b = mid
        else:
            a = mid

    return mid, f_mid, i

eps = [1e-7, 1e-15, 1e-33]
funcs = [(3*pi/2, 2*pi, f1), (10**-10, pi/2, f2), (1, 3, f3)]

print("BISECTION")
for ep in eps:
    print("EPSILON:", ep)
    for a, b, f in funcs:
        print(f"\t{bisection(a, b, f, ep, 0)}")

#jak obliczyc pierwsze k miejsc zerowych?

def Newton(a, b, func, eps, abs_error):
    def derivative(x, prev, func):
        return (func(x) - func(prev))/(x - prev)

    def calculate_new_x(x, prev, func):
        return x - func(x)/derivative(x, prev, func)
    
    n = ceil(log((b-a)/eps)/log(2))
    x = b
    prev = a
    i = 0
    while abs(x-prev) > eps and i < n:
        temp = x
        x = calculate_new_x(x, prev, func)
        prev = temp
        i += 1 
    
    return (x, func(x), i)

print("NEWTON")
for ep in eps:
    print("EPSILON:", ep)
    for a, b, f in funcs:
        print(f"\t{Newton(a, b, f, ep, 0)}")