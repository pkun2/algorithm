oriNum = set(range(1, 10001))
createdNum = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    createdNum.add(i)

selfNum = sorted(oriNum - createdNum)

for i in selfNum:
    print(i)