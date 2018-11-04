# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n <= 0: return 0
        elif n == 1: return 1
        else:
            a, b = 0, 1
            for i in range(2, n + 1):
                c = a + b
                a = b
                b = c
        return c

