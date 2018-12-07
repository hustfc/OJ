class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index < 1:
            return 0
        if index == 1:
            return 1
        uglyNumberList = [1]
        T2 , T3, T5 = 0, 0, 0
        for i in range(1, index):
            if uglyNumberList[T2] * 2 <= uglyNumberList[i - 1]:
                T2 += 1
            if uglyNumberList[T3] * 3 <= uglyNumberList[i - 1]:
                T3 += 1
            if uglyNumberList[T5] * 5 <= uglyNumberList[i - 1]:
                T5 += 1
            uglyNumber = min(uglyNumberList[T2] * 2, uglyNumberList[T3] * 3, uglyNumberList[T5] * 5) #M2 M3 M5
            uglyNumberList.append(uglyNumber)
        return uglyNumberList[index - 1]
print(Solution().GetUglyNumber_Solution(1500))