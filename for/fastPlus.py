import sys
from unittest import result

t = int(sys.stdin.readline())

for i in range(t):
    A, B = map(int, sys.stdin.readline().split())
    print(A + B)