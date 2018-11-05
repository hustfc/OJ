# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        #不保证位置一致性可以换
        # low, high = 0, len(array) - 1
        # while low < high:
        #     if low < high and array[low] & 0x1 == 1:
        #         low += 1
        #     if low < high and array[high] & 0x1 == 0:
        #         high -= 1
        #     if low < high:
        #         array[low], array[high] = array[high], array[low]
        #保证位置一致性
        Num = []
        for i in range(len(array)):
            if array[i] & 0x1 == 1:
                Num.append(array[i])
        for i in range(len(array)):
            if array[i] & 0x1 == 0:
                Num.append(array[i])
        return Num

array = [1,2,3,4,5,6,7,8,9,10]
print(Solution().reOrderArray(array))