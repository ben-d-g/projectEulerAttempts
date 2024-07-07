#https://projecteuler.net/problem=19

#set up dayCounter, increment total when at the start of a month is a sunday

class DayCounter:
    def __init__(self):
        self.day = 1 #0 represents a monday
    
    def getDay(self):
        return self.day
    
    def increment(self, days):
        self.day = (self.day + days) % 7

counter = DayCounter()
total = 0

def daysInMonth(month, year):
    if month == 1:
        if (year % 400 == 0):
            return 29
        elif (year % 4 == 0) and (year % 100 != 0):
            return 29
        else:
            return 28
    elif month in [8, 3, 5, 10]:
        return 30
    else:
        return 31
    

for year in range(1901, 2001):
    for month in range(12):
        if counter.getDay() == 6:
            total += 1
        counter.increment(daysInMonth(month, year))
        

print(total)