class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max = 0
        a = [0] * 200
        for i in range(len(s)):
            for j in range(i, len(s)):
                a[ord(s[j]) - ord('!')] += 1
                if a[ord(s[j]) - ord('!')] >= 2:
                    local_max = j - i
                    # print('local_max %d' % local_max)
                    a = [0] * 200
                    if local_max > max:
                        max = local_max
                    break
                elif j == len(s) - 1:
                    print(j)
                    local_max = j - i + 1
                    a = [0] * 200
                    if local_max > max:
                        max = local_max
        if s == " ":
            max = 1
        return max


s = 'c'
sol = Solution()
print(sol.lengthOfLongestSubstring(s))



