n = int(input())
a = list(map(int, input().split()))
m = int(input())
q = list(map(int, input().split()))
class Solution:
    def appleHeap(self, n, a, m, q):
        heap = [0] * n
        heap[0] = a[0]
        for i in range(1, n):
            heap[i] = heap[i - 1] + a[i]
        for i in range(m):
            for j in range(n):
                if q[i] > heap[j]:
                    j += 1
                else:
                    print(j + 1)
                    break;
Solution().appleHeap(n,a,m,q)


