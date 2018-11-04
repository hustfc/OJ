# -*- coding:utf-8 -*-
class Solution:
    def getDigitSum(self, num):
        sum = 0
        while num > 0:
            sum += num % 10
            num = int(num / 10)
        return sum
    def movingCore(self, threshold, rows, cols, row, col, visited):
        count = 0
        if row >= 0 and row < rows and col >= 0 and col < cols and not visited[row][col] \
            and self.getDigitSum(row) + self.getDigitSum(col) <= threshold:
            visited[row][col] = 1
            count = 1 + self.movingCore(threshold, rows, cols, row + 1, col, visited) \
            +self.movingCore(threshold, rows, cols, row - 1, col, visited) \
            +self.movingCore(threshold, rows, cols, row, col + 1, visited) \
            +self.movingCore(threshold, rows, cols, row, col - 1, visited)
        return count
    def movingCount(self, threshold, rows, cols):
        if threshold < 0 or rows <= 0 or cols <= 0:
            raise Exception('Input Error')
        visited = [([0] * cols) for i in range(rows)]
        count = self.movingCore(threshold, rows, cols, 0, 0, visited)
        return count
rows = cols = 20
print(Solution().movingCount(18, rows, cols))