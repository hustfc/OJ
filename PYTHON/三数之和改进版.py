from collections import Counter

class Solution:
    def threeSum(self, nums):
        counts = Counter(nums)
        numSet = list(set(nums))
        result = set()#使用set可以防止重复
        for i, num1 in enumerate(numSet):
            #for j, num2 in enumerate(numSet[i:]):
            for j in range(i, len(numSet))
                num3 = (num1 + num2) * -1
                #if num3 in numSet[i + j:]:
                if num3 in counts:
                    list1 = [num1, num2, num3]
                    Coun = Counter(list1)
                    shouldAdd = True
                    for num in Coun.keys():
                        if Coun[num] > counts[num]:  #比较是不是足够
                            shouldAdd = False
                    if shouldAdd:
                        result.add(tuple(sorted(list1)))   #足够
        return list(result)
nums = [-1, 0, 1, 2, -1, -4]
print(Solution().threeSum(nums))


