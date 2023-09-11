from math import *


def nto(cnt):
    if cnt < 2: return 0
    for i in range(2, int(sqrt(cnt)) + 1):
        if cnt % 2 == 0: return 0
    return 1


def cso(a, b):
    x = gcd(a, b)
    tmp = 0
    while x:
        tmp += x % 10
        x //= 10
    return tmp

t = int(input())
while t:
    a, b = map(int, input().split())
    print("YES" if nto(cso(a,b)) else "NO")
    t -= 1
