class Solution:
    def findMissNum(self, numbers):
        length = len(numbers)
        if numbers == []:
            return -1
        left = 0
        right = length - 1
        while(left <= right):
            middle = (left + right) >> 1
            if numbers[middle] != middle:
                if middle == 0 or (middle > 0 and numbers[middle - 1] == middle - 1):
                    return middle
                else:
                    right = middle - 1
            else:
                left = middle + 1
        if left == length:
            return length
        return -1
numbers = [0,1,2,3,4,5,6,7]
print(Solution().findMissNum(numbers))

