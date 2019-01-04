n = int(input())
m = int(input())
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        child = []
        if n < 1 or m < 1:
            return -1
        for i in range(n):
            child.append(i)
        temp = 0
        while len(child) > 1:
            temp = (temp + m - 1) % len(child)
            child.remove(child[temp])
        return child[0]
print(Solution().LastRemaining_Solution(n, m))
