class Solution:
    def ReverseString(self, listS, start, end):
        if listS == []:
            return []
        while start < end:
            listS[start], listS[end] = listS[end], listS[start]
            start += 1
            end -= 1
        return listS
    def ReverseSentence(self, s):
        # write code here
        if s == '':
            return ''
        start, end = 0, 0
        listS = list(s) #需要将字符串转变为数组才能更改
        self.ReverseString(listS, 0, len(s) - 1)
        while True:
            while end != len(listS) and listS[end] != ' ':
                end += 1
            end -= 1
            self.ReverseString(listS, start, end)
            if end == len(listS) - 1:
                return ''.join(listS)
            start = end + 2
            end = start
s = 'student. a am I'
print(Solution().ReverseSentence(s))
