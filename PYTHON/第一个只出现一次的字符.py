# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if s == '':
            return -1
        dic = {}
        dic = dic.fromkeys(s, 0)
        for c in s:
            dic[c] += 1
        for index, c in enumerate(s):
            if dic[c] == 1:
                return index
        return -1
print(Solution().FirstNotRepeatingChar('aabbcc'))