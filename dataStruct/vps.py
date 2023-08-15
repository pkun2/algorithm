cnt = 0
i = int(input())

for i in range(i):
    isValid = list(input())
    
    for j in isValid:
        if j in "(":
            cnt = cnt+1
        else:
            cnt = cnt-1
        if(cnt < 0):
            print("NO")
            break
        
    if(cnt > 0):
        print("NO")
    elif(cnt == 0):
        print("YES")
    cnt = 0
