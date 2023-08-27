from math import *


def nto(cnt):
    if cnt < 2: return 0
    for i in range(2, cnt):
        if n % i == 0: return 0
    return 1


def dem(n):
    cnt = 0
    for i in range(n):
        if gcd(i, n) == 1: cnt += 1
    return cnt


t = int(input())
while t > 0:
    n = int(input())
    print("YES" if nto(dem(n)) else "NO")
    t -= 1
