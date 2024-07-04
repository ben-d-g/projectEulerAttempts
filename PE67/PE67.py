#https://projecteuler.net/problem=67

#apply same technique as in PE18.py and hope that it doesn't take 7 years

txtTriangle = open("PE67triangle.txt", 'r')
array = []

while txtTriangle:
    line = txtTriangle.readline()

    if line == "":
        break

    intList = []
    strList = line.split()
    for i in strList:
        intList.append(int(i))
    array.append(intList)
    
maxSumArray = [[59]]

for i in range(1, len(array)):
    maxSumRow = []
    for j in range(len(array[i])):
        #if we are at the start of a row, only consider the start of the previous row
        if j == 0:
            maxSumRow.append(maxSumArray[i - 1][j] + array[i][j])
        #likewise for end
        elif j == len(array[i]) - 1:
            maxSumRow.append(maxSumArray[i - 1][j - 1] + array[i][j])
        #otherwise consider the element above and the element above and to the left
        else:
            maxSumRow.append(max(maxSumArray[i - 1][j] + array[i][j], maxSumArray[i - 1][j - 1] + array[i][j]))
    maxSumArray.append(maxSumRow)

for row in maxSumArray:
    for item in row:
        print(item, end = " ")
    print()

print(max(maxSumArray[-1]))