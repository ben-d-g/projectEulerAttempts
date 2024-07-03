# https://projecteuler.net/problem=2

# Binet's formula to find nth Fibonacci number

import math

phi = (1 + math.sqrt(5))/2
psi = (1 - math.sqrt(5))/2

def binet(n):
    return round((math.pow(phi, n) - math.pow(psi, n)) / math.sqrt(5))

# binet gives even fibonacci numbers as binet(3*k) for integer k

pointer = 0
total = 0

while binet(pointer) <= 4000000:
    #print(binet(pointer))
    total += binet(pointer)
    pointer += 3

print(total)