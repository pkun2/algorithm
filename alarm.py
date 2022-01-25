h, m = map(int, input().split())

if(h == 0):
    if(m < 45):
        h = 23
        m = m + 60 - 45
        print(h , m)
    elif(m >= 45):
        m = m - 45
        print(h, m)
elif(h > 0):
    if(m < 45):
        h = h - 1
        m = m + 60 - 45
        print(h , m)
    elif(m >= 45):
        m = m - 45
        print(h, m)
    