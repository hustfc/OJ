def LCS(s1, s2):
    m = len(s1)
    n = len(s2)
    c = [([0] * (n + 1)) for i in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
            else:
                c[i][j] = max(c[i - 1][j], c[i][j - 1])
    return c[m][n]

while True:
    s1 = input().strip()
    if s1 == '':
        break
    listS = list(s1)
    listS.reverse()
    s2 = ''.join(listS)
    length = len(s1)
    lcs = LCS(s1, s2)
    print(length - lcs)