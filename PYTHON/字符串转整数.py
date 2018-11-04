def isnum(x):
    if ord(x) >= ord('0') and ord(x) <= ord('9'):
        return 1
    else:
        return 0
class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        if str == '':
            return 0
        legal = 0
        string = ''
        for i in range(len(str)):
            if str[i] != ' ':
                if str[i] == '+' or str[i] == '-' or isnum(str[i]):
                    #合法的
                    if str[i] == '+' or str[i] == '-':#只有加号减号
                        if i + 1 == len(str):
                            return 0
                        elif i + 1 < len(str):
                            if not isnum(str[i + 1]):
                                return 0
                    legal = 1
                    string += str[i]
                    for j in range(i + 1, len(str)):
                        if isnum(str[j]):
                            string += str[j]
                        else:
                            break
                else:#字符开头
                    return 0
            if legal == 1:#有一个数字了
                break
        if legal == 0:
            return 0
        else:
            x = int(string)
            if x < -2 ** 31:
                return -2 ** 31
            elif x > 2 ** 31 - 1:
                return 2 ** 31 - 1
            else:
                return x
str = '3.14159'
sol = Solution()
print(sol.myAtoi(str))


