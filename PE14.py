sequenceDictionary = dict()

def collatzStep(n):
    if n % 2 == 0:
        return n / 2
    else:
        return (3 * n) + 1

def collatzSequence(n):
    seq = [n]
    while seq[-1] != 1:
        if seq[-1] in sequenceDictionary.keys():
            return seq + sequenceDictionary[seq[-1]]
        seq.append(collatzStep(seq[-1]))
    return seq

longestLength = 0
longestIndex = 0

for i in range(1, 1000000):
    ithSeq = collatzSequence(i)
    sequenceDictionary[i] = ithSeq
    if len(ithSeq) > longestLength:
        longestIndex = i
        longestLength = len(ithSeq)

print(longestIndex)