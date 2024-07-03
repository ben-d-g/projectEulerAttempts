import math

phi = (1 + math.sqrt(5))/2
psi = (1 - math.sqrt(5))/2

# as used in PE2.py
# rounding may not be suitable for large n.
def binet(n):
    return round((math.pow(phi, n) - math.pow(psi, n)) / math.sqrt(5))