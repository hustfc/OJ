class Solution:
    def partitionOfK(self, numbers, start, end, k):
        if k < 0 or numbers == [] or start < 0 or end >= len(numbers) or k > end:
            return None
        low = start
        high = end
        key = numbers[start]
        while low < high:
            while low < high and numbers[high] >= key:
                high -= 1
            numbers[low] = numbers[high]
            while low < high and numbers[low] <= key:
                low += 1
            numbers[high] = numbers[low]
        numbers[low] = key
        if low < k:
            return self.partitionOfK(numbers, start + 1, end, k)
        elif low > k:
            return self.partitionOfK(numbers, start, end - 1, k)
        else:
            return numbers[low]
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
        result = self.partitionOfK(numbers, 0, len(numbers) - 1, len(numbers) >> 2)
        if self.checkMoreThanHalf(numbers, result):
            return result
        else:
            return 0
numbers = [1,2,3,2,2,2,5,4,2]
print(Solution().MoreThanHalfNum_Solution(numbers))