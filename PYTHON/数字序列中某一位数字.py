class Solution:
    def countOfIntegers(self, digit):
        if digit == 1:
            return 10
        return 9 * (10 ** (digit - 1))
    def beginNum(self, digit):
        if digit == 1:
            return 0
        else:
            return 10 ** (digit - 1)
    def getDigit(self, digit, index):
        beginNum = self.beginNum(digit)
        endNum = beginNum + int(index / digit)
        leftIndex = index % digit
        endNumString = str(endNum)
        return endNumString[leftIndex]
    def digitAtIndex(self, index):
        if index < 0:
            raise Exception('input error')
        digit = 1
        while True:
            numbers = self.countOfIntegers(digit)
            if index < digit * numbers:
                return self.getDigit(digit, index)
            index -= numbers * digit
            digit += 1
print(Solution().digitAtIndex(0))
print(Solution().digitAtIndex(1))
print(Solution().digitAtIndex(9))
print(Solution().digitAtIndex(13))
print(Solution().digitAtIndex(19))
print(Solution().digitAtIndex(1001))