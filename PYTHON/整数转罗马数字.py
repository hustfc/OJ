class Solution(object):
    def intToRoman(self, num):
        if num == 0: return ''
        if num == 4: return 'IV'
        if num == 9: return 'IX'
        if num == 40: return 'XL'
        if num == 90: return 'XC'
        if num == 400: return 'CD'
        if num == 900: return 'CM'
        if num >= 1 and num <= 3:
            return 'I' * num
        if num >= 5 and num <= 8:
            return 'V' + self.intToRoman(num - 5)
        if num >= 10 and num <= 39:
            m = (int)(num / 10)
            return 'X' * m + self.intToRoman(num - 10 * m)
        if num > 40 and num <= 49:
            return 'XL' +self.intToRoman(num - 40)
        if num >= 50 and num < 90:
            return 'L' + self.intToRoman(num - 50)
        if num >= 90 and num <= 99:
            return 'XC' + self.intToRoman(num - 90)
        if num >= 100 and num <= 399:
            m = (int)(num / 100)
            return 'C' * m + self.intToRoman(num - m * 100)
        if num > 400 and num <= 499:
            return 'CD' + self.intToRoman(num - 400)
        if num >= 500 and num < 900:
            return 'D' + self.intToRoman(num - 500)
        if num > 900 and num <= 999:
            return 'CM' +self.intToRoman(num - 900)
        if num >= 1000 and num <= 4000:
            m = (int)(num / 1000)
            return 'M' * m + self.intToRoman(num - m * 1000)
print(Solution().intToRoman(2000))
