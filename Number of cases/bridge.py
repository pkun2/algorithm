# n! / r!(n-r)!
import math

a = int(input());

for i in range(a):
    n, r = map(int, input().split());
    result = math.factorial(r) // (math.factorial(n) * math.factorial(r-n));
    print(result);