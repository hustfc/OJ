class Solution:
    def recursionTranslate(self, string, start):
        count = 0
        if start <= len(string):
            if start == len(string):
                count += 1
            else:
                count += self.recursionTranslate(string, start + 1)
                if int(string[start:start+2]) <= 25:
                    count += self.recursionTranslate(string, start + 2)
        return count
    def translateNumToStr(self, num):
        if num <= 0:
            return 0
        else:
            return self.recursionTranslate(str(num), 0)
print(Solution().translateNumToStr(12258))