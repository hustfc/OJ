class Solution:
    # s字符串
    def scanUnsignedInteger(self, s, start, end):
        for i in range(start, end + 1):
            if not ord(s[i]) - ord('0') < 0 or ord(s[i]) - ord('0') > 9:
                return False
        return True
    def scanInteger(self, s, start, end):
        if s[start] == '+' or s[start] == '-':
            return self.scanUnsignedInteger(s, start + 1, end)
        else:
            return self.scanUnsignedInteger(s, start, end)
    def isNumeric(self, s):
        # write code here
        #数字的格式可以用A[.[B]][E|eC]或者.B[E|eC]表示，其中A和C都是整数（可以有符号也可以没有），B是一个无符号数
        index = -1
        for i in range(s):
            
