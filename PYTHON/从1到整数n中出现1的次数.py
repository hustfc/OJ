class Solution:
    def GetDigit(self, n):
        digit = 1
        while digit <= n:
            digit *= 10
        return int(digit / 10)
    def RecurtionNumber(self, n):
        if n >= 0 and n < 10:
            return 1
        digit = self.GetDigit(n)
        highOrder = int(n / digit)
        if highOrder == 1:
            return 1 + self.RecurtionNumber(n - 1)
        else:
            return (highOrder - 1) * self.RecurtionNumber(n - highOrder * digit) + digit + self.RecurtionNumber(n - highOrder * digit)
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        if n < 1:
            return 0
        return self.RecurtionNumber(n)
n = 111
print(Solution().NumberOf1Between1AndN_Solution(n))

