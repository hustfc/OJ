import math
m, n = map(int, input().split())  #整数才行
a = [0] * n  #需要规定大小，提前开辟空间
a[0] = m
sum = 0
for i in range(n - 1):
    a[i + 1] = math.sqrt(a[i])
for i in range(n):
    sum += a[i]
print("%.2f" % sum)

