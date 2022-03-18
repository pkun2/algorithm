a, b, c = map(int, input().split());

def maxofnum(a,b,c):
    max = int;
    max = a;
    if(b > max):
        max = b;
    if(c > max):
        max = c;
    return max

if(a == b and b == c):
    print(10000+(a*1000));
elif(a == b or b == c):
    print(1000+(b*100));
elif(a == c):
    print(1000+(a*100));
else:
    print(maxofnum(a,b,c) * 100);