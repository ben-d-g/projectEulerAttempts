import math

phi = (1 + math.sqrt(5))/2
psi = (1 - math.sqrt(5))/2

# as used in PE2.py
# rounding may not be suitable for large n.
def binet(n):
    return round((math.pow(phi, n) - math.pow(psi, n)) / math.sqrt(5))

def smallestPrimeDivisor(n):
    count = 2
    while True:
        if n % count == 0:
            return count
        count += 1

def primeDivisors(n):
    currentN = n
    divisors = []
    while currentN > 1:
        divisors.append(smallestPrimeDivisor(currentN))
        currentN = currentN / divisors[-1]
    return divisors

def isListPalendrome(A):
    return A == A[::-1]

def isStringPalendrome(S):
    return isListPalendrome(list(S))

def isIntPalendrome(I):
    return isStringPalendrome(str(I))

#standard summation results:

def sumOfFirstN(n):
    return (n * (n+1))/2

def sumOfFirstNSquared(n):
    return (n * (n + 1) * ((2 * n) + 1))/6

def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def firstNPrimes(n):
    primes = [2, 3]
    candidate = primes[-1] + 2
    while len(primes) + 1 <= n:
        if isPrime(candidate):
            primes.append(candidate)
        candidate += 2
    return primes

def primesUnder(n):
    primes = [2, 3]
    candidate = primes[-1] + 2
    while candidate <= n:
        if isPrime(candidate):
            primes.append(candidate)
        candidate += 2
    return primes

def divisors(n):
    divisorList = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            divisorList.append(i)
            divisorList.append(int(n/i))
    return list(set(divisorList) - {n})