class Solution:
    def FindNumsAppearOnce(self, array):
        # write code here
        result = 0
        for i in array:
            result = result ^ i
        return result
array = [1,2,3,4,5,6,5,4,3,2,1]
print(Solution().FindNumsAppearOnce(array))