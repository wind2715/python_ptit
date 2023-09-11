t = int(input())
while t:
    res = input()
    tmp = ''.join(sorted(res))
    if res == tmp:
        print("YES")
    else:
        print("NO")
    t -= 1
