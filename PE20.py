#https://projecteuler.net/problem=20

#first attempt, simply calculate 100!, convert to string, sum each digit

import toolbox

factStr = str(toolbox.factorial(100))

total = 0

for char in factStr:
    total += int(char)

print(total)

