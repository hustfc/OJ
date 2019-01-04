c = [([0] * 105) for i in range(105)]
mod = 1000000007
c[0][0] = 1
for i in range(1, 101):
    c[i][0] = 1
    for j in range(1, 101):
        c[i][j] = (c[i - 1][j - 1] + c[i - 1][j]) % mod    #杨辉三角形
K = int(input())
A, X, B, Y = map(int, input().split())
ans = 0
for x in range(X + 1):
    y = int((K - A * x) / B)  #第二个歌单的数量
    if x * A <= K and (K - A * x) % B == 0 and y <= Y:
        ans = (ans + (c[X][x] * c[Y][y]) % mod) % mod
print(ans)