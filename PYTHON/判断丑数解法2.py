class Solution:
    def isUglyNum(self, num):
        while num % 2 == 0:
            num /= 2
        while num % 3  == 0:
            num /= 3
        while num % 5 == 0:
            num /= 5
        if num == 1:
            return 1
        return 0
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index < 1:
            return 0
        if index == 1:
            return 1
        result = 1
        count = 1
        while True:
            result += 1
            if self.isUglyNum(result):
                count += 1
            if count == index:
                return result
print(Solution().GetUglyNumber_Solution(1500))