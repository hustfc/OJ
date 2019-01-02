n, m = map(int, input().split())
start = m - (n - 1)
count = 0
while start >= 1:
    eat = start
    day = 1
    while day <= n:
        count += eat
        if eat & 0x01 == 0:
            eat = int(eat / 2)
        else:
            eat = int(eat / 2) + 1
        if eat < 1:
            eat = 1
        day += 1
    if count <= m:
        print(start)
        break
    start -= 1
    count = 0