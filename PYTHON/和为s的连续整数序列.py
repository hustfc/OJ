class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum < 3:
            return []
        small, big = 1, 2
        results = []
        sum = small + big
        while small < tsum / 2:
            if sum < tsum:
                big += 1
                sum += big
            elif sum > tsum:
                sum -= small
                small += 1
            else:
                results.append(list(range(small, big + 1)))
                sum -= small
                small += 1
        return results
print(Solution().FindContinuousSequence(100))