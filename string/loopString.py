loopnum = int(input());

for _ in range(loopnum):
    l, s = input().split();
    r = "";
    for i in s:
       r += int(l) * i; 
    print(r);