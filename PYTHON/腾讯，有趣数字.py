import sys
def TowTuple(n, a):
    a.sort()
    minA, maxA = 1, 1
    for i in range(1, n):
        if a[i] == a[0]:
            minA += 1
        else:
            break
    for i in range(n - 2, - 1, -1):
        if a[i] == a[n - 1]:
            maxA += 1
        else:
            break
    ans2 = minA * maxA
    minDiffer = 1000000
    ans1 = 0
    for i in range(1, n):  #找出最小差值
        differ = a[i] - a[i - 1]
        if differ < minDiffer:
            minDiffer = differ
    for i in range(0, n):
        for j in range(i + 1, n):
            if a[j] - a[i] == minDiffer:
                ans1 += 1
            elif a[j] - a[i] > minDiffer:   #超时的举措，将后面的全部掐掉
                break
    return ans1, ans2
try:
    while True:
        line1 = sys.stdin.readline().strip()
        line2 = sys.stdin.readline().strip()
        if line1 == '':
            break
        n = int(line1)
        a = list(map(int, line2.split()))
        ans1, ans2 = TowTuple(n, a)
        print(ans1, ans2)
except:
    pass
