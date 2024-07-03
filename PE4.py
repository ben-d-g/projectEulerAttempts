# https://projecteuler.net/problem=4

import toolbox

palendromeProducts = []

for i in range(1000, 100, -1):
    for j in range(1000, i-1, -1):
        if toolbox.isIntPalendrome(i * j):
            palendromeProducts.append(i*j)

print(max(palendromeProducts))