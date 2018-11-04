class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        for i in range(len(s)):
            for j in range(len(s) - 1, i, -1):
                for m in range(i, j + 1):
                    if a[m] == a[j - m]