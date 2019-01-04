n = int(input())
a = list(map(int, input().split()))
k, d = map(int, input().split())
maxVal = [([0] * k) for i in range(n)]
minVal = [([0] * k) for i in range(n)]
for i in range(n):
    maxVal[i][0] = minVal[i][0] = a[i]
result = 0
for i in range(n):
    for j in range(1, k):
        for c in range(i - 1, max(i - d, 0) - 1, -1):
            maxVal[i][j] = max(maxVal[i][j], max(maxVal[c][j - 1] * a[i], minVal[c][j - 1] * a[i]))
            minVal[i][j] = min(minVal[i][j], min(maxVal[c][j - 1] * a[i], minVal[c][j - 1] * a[i]))
    result = max(result, max(maxVal[i][k - 1], minVal[i][k - 1]))
print(result)