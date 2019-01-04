#s = input()
def LCS(s1, s2):
    m = len(s1)
    n = len(s2)
    c = [([0] * (n + 1)) for i in range(m + 1)] # c[s1][s2]
    b = [([0] * (n + 1)) for i in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = 1    #左上搜索
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                b[i][j] = 2  # 向上搜索
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = 3  # 左边搜索
            #print(c)
    return c[m][n]
s1 = 'ABCBDAB'
s2 = 'BDCABA'
print(LCS(s1, s2))

