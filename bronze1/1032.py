n = int(input())

cnt = 0
tmp = n

while(1):
    cnt += 1
    ten = tmp // 10
    one = tmp % 10
    
    tmp = one*10 + ((ten + one) % 10)
    if(n == tmp):
        break
    
print(cnt)