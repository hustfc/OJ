class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        按照行索引
        """
        # array = ['!'] * 10
        # rows = [array] * numRows #二维数组
        rows = [(['!'] * 1000) for i in range (numRows)]
        rowindex = [0] * numRows #记录每一行元素的个数
        row = 0
        for i in s:
            if row == 0:
                step = 1
            if row == numRows - 1:
                step = -1
            if numRows == 1:
                return s
            rows[row][rowindex[row]] = i
            print('rows[%d][%d] = %c' % (row, rowindex[row], rows[row][rowindex[row]]))
            #print(rows)
            rowindex[row] += 1
            row += step
        #print(rows)
        str1 = ''
        # for i in range(numRows):
        #     for j in rows[i]:
        #         if j != '!':
        #             str1 = str1 + j
        # return str1
        for i in rows:
            print(i)

s = 'ABCfdafa'
numRows = 3
sol = Solution()
print(sol.convert(s, numRows))




