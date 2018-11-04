# -*- coding:utf-8 -*-
class Solution:
    def myPower(self, base, exponent):
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        result = self.myPower(base, exponent >> 1)  #注意位运算要比乘除运算和取余运算效率高很多
        result = result * result
        if exponent & 0x1 == 1:
            result *= base
        return result
    def Power(self, base, exponent):
        # write code here
        if base == 0 and exponent <= 0:
            return 0
        flag = 0
        if exponent < 0:
            flag = 1
        exponent = abs(exponent)
        result = self.myPower(base, exponent)
        if flag == 1:
            result = (float)(1 / result)
        return result
print(Solution().Power(0,-1))
