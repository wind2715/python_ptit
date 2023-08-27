t = int(input())
while t>0:
    res = input()
    ok=1
    for i in res:
        if i!='4' and i!='7':
            ok=0
            break
    if not ok: print("NO")
    else: print("YES")
    t-=1