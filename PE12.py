# https://projecteuler.net/problem=12

import toolbox

# triangular numbers are given by sum formula in toolbox
# while loop until we find a highly divisible candidate

counter = 1

while len(toolbox.divisors(toolbox.sumOfFirstN(counter))) < 500:
    #print(len(toolbox.divisors(toolbox.sumOfFirstN(counter))))
    counter += 1

print(counter)
print(toolbox.sumOfFirstN(12375))