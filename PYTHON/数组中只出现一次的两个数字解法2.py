class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        if array == []:
            return []
        result = []
        for i in array:
            if array.count(i) == 1 and i not in result:
                result.append(i)
        return result
array = [1,2,3,4,5,6,5,4,3,2]
print(Solution().FindNumsAppearOnce(array))