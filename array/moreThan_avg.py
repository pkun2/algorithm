c = int(input())
avg = []

for i in range(c):
    n = list(map(int, input().split()))
    sum = 0
    
    for i in range(n[0]):
        sum += n[i + 1]
        
    mtn = 0
    for i in range(n[0]):
        if (n[i + 1] > sum/n[0]):
            mtn += 1
    
    avg.append(mtn/n[0] * 100)
    
for i in range(c):
    print("%.3f" %avg[i] + "%")