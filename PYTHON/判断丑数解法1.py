# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.uglyList = []
    def isUglyNum(self, Num):
        num = Num
        while num % 2 == 0:
            num = (int)(num / 2)
            if self.uglyList[num] == 1:
                self.uglyList[Num] = 1
                return 1
        while num % 3  == 0:
            num = (int)(num / 3)
            if self.uglyList[num] == 1:
                self.uglyList[Num] = 1
                return 1
        while num % 5 == 0:
            num = (int)(num / 5)
            if self.uglyList[num] == 1:
                self.uglyList[Num] = 1
                return 1
        if num == 1:
            return 1
        return 0
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index < 1:
            return 0
        if index == 1:
            return 1
        self.uglyList = [0] * (index ** 4)
        self.uglyList[1] = 1
        result = 1
        count = 1
        while True:
            result += 1
            if self.isUglyNum(result):
                count += 1
            if count == index:
                return result
print(Solution().GetUglyNumber_Solution(1500))