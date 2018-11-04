class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        string = str(x)
        i, j = 0, len(string) - 1
        while i != j:
            if string[i] != string[j]:
                return False
            if i == len(string) / 2:
                return True
            i += 1
            j -= 1
        return True
x = 12321
sol = Solution()
print(sol.isPalindrome(x))
