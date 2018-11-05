class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        #数字的格式可以用A[.[B]][E|eC]或者.B[E|eC]表示，其中A和C都是整数（可以有符号也可以没有），B是一个无符号数
        #采用遍历的方式发现很困难的时候，需要采取聪明一点的方式
        #如果遍历到e，那么之前不能有e，并且e不能在末尾
        #如果遍历到.,那么之前不能有.，并且之前不能有e
        #如果遍历到符号，那么如果之前有符号，只能够出现在e的后面
        hasE = False
        hasDot = False
        hasSign = False
        for i in range(len(s)):
            if s[i] == 'e' or s[i] == 'E':
                if hasE or i == len(s) - 1:
                    return False
                hasE = True
            elif s[i] == '.':
                if hasDot or hasE:
                    return False
                hasDot = True
            elif s[i] == '+' or s[i] == '-':
                if hasSign and s[i - 1] != 'e' and s[i - 1] != 'E':
                    return False
                if not hasSign:
                    if i != 0 and s[i - 1] != 'e' and s[i - 1] != 'E':
                        return False
                hasSign = True
            else:
                if s[i] < '0' or s[i] > '9':
                    return False
        return True
print(Solution().isNumeric('12e'))
