class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        排序数组，可以首先通过两个数组的大小确定中位数的位置
        然后通过比较两个数组的元素大小，直接找出中位数
        """
        len1 = len(nums1)
        len2 = len(nums2)
        length = len1 + len2
        nums = [0] * length
        i, j, f1, f2 = 0, 0, 0, 0
        if len1 == 0:
            nums = nums2
        elif len2 == 0:
            nums = nums1
        else:
            for index in range(length):
                if nums1[i] < nums2[j] and f1 == 0:
                    nums[index] = nums1[i]
                    if i != len1 - 1:
                        i += 1
                    else:
                        f1 = 1
                elif nums1[i] < nums2[j] and f1 == 1:
                    nums[index] = nums2[j]
                    if j != len2 - 1:
                        j += 1
                elif nums1[i] >= nums2[j] and f2 == 0:
                    nums[index] = nums2[j]
                    if j != len2 - 1:
                        j += 1
                    else:
                        f2 = 1
                else:
                    nums[index] = nums1[i]
                    if i != len1 - 1:
                        i += 1
        print(nums)
        if length % 2 == 1:
            return nums[int(length / 2)]
        else:
            Median_index1 = int(length / 2) - 1
            Median_index2 = int(length / 2)
            return float((nums[Median_index1] + nums[Median_index2]) / 2)

nums1 = [ ]
nums2 = [1]
sol = Solution()
print(sol.findMedianSortedArrays(nums1, nums2))
