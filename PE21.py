# https://projecteuler.net/problem=21

from toolbox import divisors

def d(n):
    return(sum(divisors(n)))

amicableNums = []

for i in range(2, 10001):
    d_i = d(i)
    if d_i <= 10000 and d(d_i) == i and d_i != i:
        amicableNums.append(i)
        amicableNums.append(d_i)
        print(i, d_i)


print(sum(set(amicableNums)))