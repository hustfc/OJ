class Solution:
    def Increment(self, number):
        overFlow = carry = 0
        length = len(number)
        for i in range(length - 1, -1, -1):
            num = ord(number[i]) - ord('0') + carry
            if i == length - 1:#只有最后一个数加一，其他数加carry位
                num += 1
            if num >= 10:
                if i == 0:
                    overFlow = 1
                else:
                    num -= 10
                    carry = 1
            else:
                carry = 0
            number[i] = chr(ord('0') + num)   #chr将数组转化为ascii
        return overFlow
    def PrintNum(self, number):
        string = ''.join(number)
        for i in range(len(string)):
            if string[i] != '0':
                print(string[i:])
                break
    def print1ToMaxOfNDigits(self, n):
        if n <= 0:
            raise Exception('Input Error : n!')
        #n可能为很大的数，因此需要使用数组来模拟，最后再使用join方法
        number = ['0'] * n  #需要用字符表示，然后才能join
        #！！！list是可变对象，作为函数参数进行传递的时候，会改变他的值
        while not self.Increment(number):
            self.PrintNum(number)
Solution().print1ToMaxOfNDigits(9)

