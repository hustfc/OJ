numbers = list(map(int, input().split()))
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        # 由于扑克牌是0~13的数字，因此可以使用hash表来排序，并且hash表可以用来检测重复
        if numbers == []:
            return False
        hashNum = [0] * 14
        for num in numbers:
            if num != 0 and hashNum[num] != 0:
                return False
            hashNum[num] += 1
        space = 0 #统计空缺的数目
        sortNums = []
        for i in range(1, 14):
            if hashNum[i] != 0:
                sortNums.append(i)
                if len(sortNums) >= 2:
                    space += sortNums[len(sortNums) - 1] - sortNums[len(sortNums) - 2] - 1
        #print(space, hashNum[0], sortNums)
        if space <= hashNum[0]:
            return True
        else:
            return False
print(Solution().IsContinuous(numbers))


