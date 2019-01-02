s = input()
n = int(input())
class Solution:
    def ReverseList(self, nums, start, end):
        if nums == []:
            return nums
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        return nums
    def LeftRotateString(self, s, n):
        # write code here
        if s == []:
            return s
        if n <= 0:
            return s
        listString = list(s)
        leftReverse = self.ReverseList(listString, 0, n - 1)
        rightReverse = self.ReverseList(leftReverse, n, len(s) - 1)
        resultList = self.ReverseList(rightReverse, 0, len(s) - 1)
        return ''.join(resultList)
print(Solution().LeftRotateString(s, n))