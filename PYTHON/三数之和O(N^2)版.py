class Solution:
    def isNotSame(self, lists, list):  # 判断是否重复函数
        for i in range(len(lists)):
            if list == lists[i]:
                return False
        return True
    def threeSum(self, nums):
        lists = []
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums[i + 1:]):
                num3 = (num1 + num2) * -1
                if num3 in nums[i + j + 2:]:    #注意这里是i + j + 2因为总是从nums开始数的(m = j + 1)
                    list = [num1, num2, num3]
                    list.sort()
                    if self.isNotSame(lists, list):
                        lists.append(list)
        return lists
nums = [-1, 0, 1, 2, -1, -4]
print(Solution().threeSum(nums))
