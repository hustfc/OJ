class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, num in enumerate(nums):
            sub_num = target - num
            if sub_num in nums:
                j = nums.index(sub_num)
                if j != i:
                    return [i, j]
