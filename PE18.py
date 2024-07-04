# https://projecteuler.net/problem=18

#I would like my approach to this to be creating a second triangle of max path sum to each element

#initialise array
array = [[75],
[95, 64],
[17, 47, 82],
[18, 35, 87, 10],
[20, 4, 82, 47, 65],
[19, 1, 23, 75, 3, 34],
[88, 2, 77, 73, 7, 63, 67],
[99, 65, 4, 28, 6, 16, 70, 92],
[41, 41, 26, 56, 83, 40, 80, 70, 33],
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
[63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
[4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

maxSumArray = [[75]]

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