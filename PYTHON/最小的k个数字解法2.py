# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if tinput == [] or k <= 0 or k > len(tinput):
            return []
        result = []
        for num in tinput:
            if len(result) < k:
                result.append(num)
            else:
                if num < max(result):
                    result[result.index(max(result))] = num
        return sorted(result)
tinput = [4,5,1,6,2,7,3,8]
k = 5
print(Solution().GetLeastNumbers_Solution(tinput, k))