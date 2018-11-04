# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        if n == 0: return 0
        count = 0
        while n != 0:
            m = n - 1
            n = n & m
            count += 1
        return count
print(Solution().NumberOf1(1923432))