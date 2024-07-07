#https://projecteuler.net/problem=22

def score(name):
    total = 0
    for char in name:
        total += "ABCDEFGHIJKLMNOPQRSTUVWXYZ".index(char) + 1
    return total

namesFile = open("names.txt", "r")
namesString = namesFile.read()
namesStrings = namesString.split(",")
namesStrings.sort() #we do not need to remove '"'s

total = 0

for nameIndex in range(len(namesStrings)):
    #now we do
    total += score(namesStrings[nameIndex][1:-1]) * (nameIndex + 1)

print(total)