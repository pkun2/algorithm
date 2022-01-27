A = int(input())

for i in range(1, A+1):
    f, s = map(int, input().split())
    print("Case #%s: %s + %s = %s" %(i, f, s, f+s))
    #print("Case #%s:" %(i), f, "+", s, "=", f+s)