class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if len(array) <= 1:
            return []
        low, high = 0, len(array) - 1
        results = []
        while low < high:
            if array[low] + array[high] == tsum:
                results.append([array[low], array[high]])
                low += 1
                high -= 1
            elif array[low] + array[high] < tsum:
                low += 1
            else:
                high -= 1
        if results == []:
            return []
        minMutiple = results[0][0] * results[0][1]
        minindex = 0
        for i, result in enumerate(results):
            if result[0] * result[1] < minMutiple:
                minMutiple = result[0] * result[1]
                minindex = i
        return results[minindex]
array = [1,2,4,7,11,16]
print(Solution().FindNumbersWithSum(array, 10))