# https://projecteuler.net/problem=9

import math

def getTriple(m,n):
    a = m**2 - n**2
    b = 2 * m * n
    c = m**2 + n**2
    return a,b,c

def findIt():
    for m in range(1, 1000):
        for n in range(1, m):
            a, b, c = getTriple(m,n)
            k = 1
            while k * (a + b + c) <= 1000:
                if k * (a + b + c) == 1000:
                    return k*a, k*b, k*c
                k += 1

a,b,c = findIt()

print("a =", a, ", b =", b, " c =", c)
print(a * b * c)