# https://projecteuler.net/problem=17

#Counting the number of letters required to write the numbers 1 to 1000
#I do not enjoy this task

#set up digit dictionary
digits = {
    0: 0, # this is not the number of letters in "zero" but makes the if statements nicer later on
    1: 3,
    3: 5,
    2: 3,
    4: 4,
    5: 4,
    6: 3,
    7: 5,
    8: 5,
    9: 4,
    10: 3,
    11: 6,
    12: 6,
    13: 8,
    14: 8,
    15: 7,
    16: 7,
    17: 9,
    18: 8,
    19: 8,
    20: 6,
    30: 6,
    40: 5,
    50: 5,
    60: 5,
    70: 7,
    80: 6,
    90: 6,
    100: 7,
    1000: 8
}

#counting function
def howManyLetters(n):
    #we have 1 - 19 hard coded
    if n <= 20:
        return digits[n]
    #for the rest we can split it into large part/small part
    elif n % 10 == 0 and n < 100:
        return digits[n]
    elif n < 100:
        return howManyLetters(n - (n % 10)) + howManyLetters(n % 10)
    elif n == 1000:
        return digits[1] + digits[1000]
    elif n % 100 == 0:
        return digits[n / 100] + digits[100]
    else:
        return howManyLetters(n - (n % 100)) + 3 + howManyLetters(n % 100)

total = 0
for i in range(1, 1001):
    total += howManyLetters(i)
print(total)