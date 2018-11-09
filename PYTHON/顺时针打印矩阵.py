# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrixCore(self, matrix, row, col, mode, visited):
        result = []
        result.append(matrix[row][col])
        visited[row][col] = 1
        if mode == 1:
            if row < len(matrix) and col + 1 < len(matrix[0]) and visited[row][col + 1] == 0:
                result += self.printMatrixCore(matrix, row, col + 1, 1, visited)
            elif row + 1 < len(matrix) and col < len(matrix[0]) and visited[row + 1][col] == 0:
                result += self.printMatrixCore(matrix, row + 1, col, 2, visited)
        elif mode == 2:
            if row + 1 < len(matrix) and col < len(matrix[0]) and visited[row + 1][col] == 0:
                result += self.printMatrixCore(matrix, row + 1, col, 2, visited)
            elif row >= 0 and col - 1 >= 0 and visited[row][col - 1] == 0:
                result += self.printMatrixCore(matrix, row, col - 1, 3, visited)
        elif mode == 3:
            if row >= 0 and col - 1 >= 0 and visited[row][col - 1] == 0:
                result += self.printMatrixCore(matrix, row, col - 1, 3, visited)
            elif row - 1 >= 0 and col >= 0 and visited[row - 1][col] == 0:
                result += self.printMatrixCore(matrix, row - 1, col, 4, visited)
        elif mode == 4:
            if row - 1 >= 0 and col >= 0 and visited[row - 1][col] == 0:
                result += self.printMatrixCore(matrix, row - 1, col, 4, visited)
            elif row < len(matrix) and col + 1 < len(matrix[0]) and visited[row][col + 1] == 0:
                result += self.printMatrixCore(matrix, row, col + 1, 1, visited)
        return result
    def printMatrix(self, matrix):
        # write code here
        try:
            cols = len(matrix[0])
        except:
            raise Exception('输入矩阵必须为二维矩阵')
        visited = [([0] * cols) for i in range(len(matrix))]
        return self.printMatrixCore(matrix, 0, 0, 1, visited)
matrix = [1,2,3,4]
print(Solution().printMatrix(matrix))

