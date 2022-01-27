N = oNum = int(input())
cyc = 0

while 1:
    t = N // 10
    o = N % 10
    sum = t + o
    cyc += 1
    N = int(str(N % 10) + str(sum % 10))
    if(N == oNum):
        break
print(cyc)