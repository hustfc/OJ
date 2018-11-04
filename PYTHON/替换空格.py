# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        spaceNum = 0
        for c in s:
            if c == ' ':
                spaceNum += 1
        lenString = len(s) + spaceNum * 2
        p ,q = len(s) - 1, lenString - 1
        string = ['1'] * lenString
        while p != -1:
            if s[p] != ' ':
                string[q] = s[p]
                p -= 1
                q -= 1
            else:
                string[q] = '0'
                string[q - 1] = '2'
                string[q - 2] = '%'
                p -= 1
                q -= 3
        return ''.join(string)