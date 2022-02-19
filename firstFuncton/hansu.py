num = int(input())
hansu = 0

for i in range(1, num+1):
    numList = list(map(int, str(i)))
    if (i < 100):
        hansu += 1
    elif (numList[0] - numList[1] == numList[1] - numList[2]):
        hansu += 1

print(hansu)