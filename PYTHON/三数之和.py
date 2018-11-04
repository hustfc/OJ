class Solution(object):
    def isNotSame(self, lists, list):  # 判断是否重复函数
        for i in range(len(lists)):
            if list == lists[i]:
                return False
        return True

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        lists = []
        nums.sort()
        if len(nums) < 3: return lists
        for i in range(len(nums) - 1):
            if i < len(nums) - 2 and nums[i + 1] == 0 and nums[i + 1] + nums[i] + nums[i + 2] == 0:
                index = i
                list = [nums[i + 1], nums[i], nums[i + 2]]
                list.sort()
                lists.append(list)
                break
            if nums[i] < 0 and nums[i + 1] >= 0:
                index = i
                break  # 防止挑不出来
        if i == 0 and nums[i] == 0:
            if nums[i] + nums[i + 1] + nums[i + 2] == 0:
                return [[0, 0, 0]]
        # [1,1,1]找不到index
        if i == len(nums) - 2 and nums[i] != 0 and nums[i + 1] != 0:
            return []

        for i in range(index + 1):
            for j in range(index + 1, len(nums)):
                for m in range(i + 1, index + 1):
                    if nums[m] + nums[i] + nums[j] == 0:
                        list = [nums[m], nums[i], nums[j]]
                        list.sort()
                        if self.isNotSame(lists, list):
                            lists.append(list)
                for m in range(j + 1, len(nums)):
                    if nums[m] + nums[i] + nums[j] == 0:
                        list = [nums[m], nums[i], nums[j]]
                        list.sort()
                        if self.isNotSame(lists, list):
                            lists.append(list)
        return lists


nums = [-1,0,1,2,-1,-4]
print(Solution().threeSum(nums))




