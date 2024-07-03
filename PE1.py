# https://projecteuler.net/problem=1

# find the sum of all multiples of 3 or 5 between 0 and 1000

listOfIntegers = list(range(1, 1000))
listOfMultiples = [u for u in listOfIntegers if (u % 3 == 0 or u % 5 == 0)]

print(sum(listOfMultiples))