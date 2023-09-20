a = input()
b = int(input())

tmp = int(a[:-2] + "00")

while(1):
    if(tmp % b == 0):
        break
    tmp = tmp + 1

print(str(tmp)[-2:])