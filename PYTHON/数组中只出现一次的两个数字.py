class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        if array == []:
            return []
        dic = {}
        for i in array:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        result = []
        for j in dic:
            if dic[j] == 1:
                result.append(j)
        return result
array = [1,2,3,4,5,6,5,4,3,2]
print(Solution().FindNumsAppearOnce(array))