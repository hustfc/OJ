n, k = map(int, input().split())
interest = list(map(int, input().split()))
awake = list(map(int, input().split()))
class Solution:
    def maxScore(self, n, k , interest, awake):
        score = 0
        addScore = 0
        i = 0
        add = 0
        while i < n:
            if awake[i] == 1:
                score += interest[i]
                i += 1
            else:
                j = 0
                while j < k:
                    if i + j < n and awake[i + j] == 0:
                        if add == 0:
                            add += interest[i + j]
                    j += 1
                if add > addScore:
                    addScore = add
                add = 0
                i += 1
        return score + addScore
print(Solution().maxScore(n,k,interest,awake))
