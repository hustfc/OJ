# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def matchCore(self, s, pattern, startS, startP):
        #print(startS, startP)
        if startS == len(s) and startP == len(pattern):
            return True
        if startP < len(pattern) - 1 and pattern[startP + 1] == '*':
            if (startS < len(s) and pattern[startP] == s[startS]) or (pattern[startP] == '.' and startS < len(s)):
            #     # abc  和 ab*c匹配
            #     # abbc 和 ab*c匹配
            #     # aaa  和 aa*aa匹配

                return self.matchCore(s, pattern, startS + 1, startP + 2) or \
                    self.matchCore(s, pattern, startS + 1, startP) or \
                    self.matchCore(s, pattern, startS, startP + 2)
            else:
                return self.matchCore(s, pattern, startS, startP + 2)     #*前面的字母不一样，直接跳过*
        if startS < len(s) and startP < len(pattern):   #必须要判断是否越界
            if pattern[startP] == '.' or pattern[startP] == s[startS]:
                return self.matchCore(s, pattern, startS + 1, startP + 1)
        return False
    def match(self, s, pattern):
        # write code here
        if s == '' and pattern == '':
            return True
        return self.matchCore(s, pattern, 0, 0)
print(Solution().match('a','.'))




