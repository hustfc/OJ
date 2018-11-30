class Solution:
    def GetSum(self, array, start, end):
        sum = 0
        for i in range(start, end + 1):
            sum += array[i]
        return sum
    def EvaluateSum(self, array, index, subArraySum, flag):
        if index == 0 or index == len(array) - 1:
            return array[index]
        else:
            if flag:
                return subArraySum[0][index - 1] + array[index]
            else:
                return subArraySum[1][index + 1] + array[index]
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        flag = 1
        subArraySum = [([0] * len(array)) for i in range(2)]
        low, high = 0, len(array) - 1
        i = low + 1
        j = high - 1
        subArraySum[0][0] = array[0]
        subArraySum[1][len(array) - 1] = array[len(array) - 1]
        while low < high:
            if low < high and flag:
                for i in range(low + 1, high + 1):
                    subArraySum[0][i] = self.EvaluateSum(array, i, subArraySum, flag)
                    if subArraySum[0][i - 1] < 0:
                        low = i
                        flag = 0
                        break
            elif low < high and not flag:
                for j in range(high - 1, low - 1, -1):
                    subArraySum[1][j] = self.EvaluateSum(array, j, subArraySum, flag)
                    if subArraySum[1][j + 1] < 0:
                        high = j
                        flag = 1
                        break
            if i == high or j == low:  #跳出主循环，防止找不到更大的，low和high不改变一致循环
                break
        return self.GetSum(array, low, high)
array = [1,-2,3,10,-4,7,2,-5]
print(Solution().FindGreatestSumOfSubArray(array))