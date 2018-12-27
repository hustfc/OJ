n, m = map(int, input().split())
nums = map(int, list(input().split()))
class Solution:
    def AddScore(self, dic):
        for i in dic:
            if dic[i] < 1:
                return False
        return True
    def Score(self, n, nums):
        score = 0
        dic = {}
        dic = dic.fromkeys(range(1, n + 1), 0)
        for num in nums:
            dic[num] += 1
            if self.AddScore(dic):
                score += 1
                for i in dic:
                    dic[i] -= 1
        return score
print(Solution().Score(n, nums))