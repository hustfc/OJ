class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if array == []:
            return 0
        if len(array) == 1:
            return array[0]
        maxSum = totalSum = array[0]
        #low = 0
        for i in range(1, len(array)):
            totalSum += array[i]
            print(i, array[i], totalSum, maxSum)
            if array[i] > totalSum:
                #low = i
                totalSum = array[i]
                if array[i] > maxSum:
                    maxSum = array[i]
            else:
                if totalSum > maxSum:
                    maxSum = totalSum
        return maxSum
array = [-2,-8,-1,-5,-9]
print(Solution().FindGreatestSumOfSubArray(array))
