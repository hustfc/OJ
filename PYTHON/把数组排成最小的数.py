class Solution:
    def myCmp(self, num1, num2):
        string1 = str(num1) + str(num2)
        string2 = str(num2) + str(num1)  #防止整数越界
        if len(string1) < len(string2) or (len(string1) == len(string2) and string1 < string2):
            return 1
        return 0
    def myQuickSort(self, numbers, start, end):
        if start < 0 or end >= len(numbers) or start >= end:
            return
        low, high = start, end
        key = numbers[low]
        while low < high:
            while low < high and self.myCmp(key, numbers[high]):
                high -= 1
            numbers[low] = numbers[high]
            while low < high and not self.myCmp(key, numbers[low]):
                low += 1
            numbers[high] = numbers[low]
        numbers[low] = key
        self.myQuickSort(numbers, start, low - 1)
        self.myQuickSort(numbers, low + 1, end)
    def PrintMinNumber(self, numbers):
        if numbers == []:
            return ''
        self.myQuickSort(numbers, 0, len(numbers) - 1)
        string = ''
        for num in numbers:
            string += str(num)
        return string
numbers = [3,32,321]
print(Solution().PrintMinNumber(numbers))
