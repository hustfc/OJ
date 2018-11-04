# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        count = 0
        if number < 1: return 0
        if number == 1: return 1
        if number == 2: return 2
        count = 2 + self.rectCover(number - 2)
        return count
