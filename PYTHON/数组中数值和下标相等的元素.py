class Solution:
    def numberEqualSubscript(self, numbers):
        if numbers == []:
            return -1
        left = 0
        right = len(numbers) - 1
        while(left <= right):
            middle = (left + right) >> 1
            if numbers[middle] == middle:
                return middle
            elif numbers[middle] < middle:
                left = middle + 1
            else:
                right = middle - 1
        return -1
numbers = [-3,-1,1,3,5]
print(Solution().numberEqualSubscript(numbers))