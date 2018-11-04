# -*- coding:utf-8 -*-
class Solution:
    def minArray(self, array, low, high):
        minElem = array[low]
        for i in range(low, high + 1):
            if array[i] < minElem:
                minElem = array[i]
        return minElem
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            raise Exception('Invalid input!')
        low, high = 0, len(rotateArray) - 1
        while(rotateArray[low] >= rotateArray[high]):
            if low + 1 == high:
                return rotateArray[high]
            mid = int((low + high) / 2)
            if rotateArray[mid] == rotateArray[low] and rotateArray[mid] == rotateArray[high]:
                return self.minArray(rotateArray, low, high)
            if rotateArray[mid] >= rotateArray[low]:
                low = mid
            else:
                high = mid
        return rotateArray[low]   #数组是按照顺序排列的情况

array = [1,2,3,4,5]
print(Solution().minNumberInRotateArray(array))
