# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if numbers == []:
            return 0
        dictonary = {}
        dictonary = dictonary.fromkeys(numbers, 0)
        for num in numbers:
            dictonary[num] += 1
        for key in dictonary.keys():
            if dictonary[key] * 2 > len(numbers):
                return key
        return 0
numbers = [1,2,3,2,2,2,5,4,2]
print(Solution().MoreThanHalfNum_Solution(numbers))