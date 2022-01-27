A = int(input())

for i in range(1, A+1):
    f, s = map(int, input().split())
    print("Case #%s: %s" %(i, f+s))