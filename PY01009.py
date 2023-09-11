res = input()
cnt = 0
for i in res:
    if 'a' <= i <= 'z':
        cnt += 1
if cnt >= len(res)/2:
    print(res.lower())
else: print(res.upper())