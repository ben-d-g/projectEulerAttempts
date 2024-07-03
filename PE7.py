# https://projecteuler.net/problem=7

import toolbox

def firstNPrimes(n):
    primes = [2, 3]
    candidate = primes[-1] + 2
    while len(primes) + 1 <= n:
        if toolbox.isPrime(candidate):
            primes.append(candidate)
        candidate += 2
    return primes

print(firstNPrimes(10001)[-1])