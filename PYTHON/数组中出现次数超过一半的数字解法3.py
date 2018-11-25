# -*- coding:utf-8 -*-
class Solution:
    def checkMoreThanHalf(self, numbers, num):
        times = 0
        for number in numbers:
            if num == number:
                times += 1
        if times * 2 <= len(numbers):
            return False
        return True
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if numbers == []:
            return 0
        result = numbers[0]
        times = 1
        for i in range(1, len(numbers)):
            if times == 0:
                result = numbers[i]
                times = 1
            elif numbers[i] == result:
                times += 1
            else:
                times -= 1
        if self.checkMoreThanHalf(numbers, result):
            return result
        else:
            return 0
numbers = [1,2,3,2,2,2,5,4,2]
print(Solution().MoreThanHalfNum_Solution(numbers))
