test = int(input())
while test > 0:
    n = int(input())
    b = 0
    s = ""
    while n > 10:
        a = n % 10 + b
        b = 1 if a >= 5 else 0
        s = "0" + s
        n //= 10
    print(f"{n + b}{s}")
    test -= 1
