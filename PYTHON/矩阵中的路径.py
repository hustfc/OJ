# -*- coding:utf-8 -*-
class Solution:
    def hasPathCore(self, matrix, rows, cols, row, col, path, pathIndex, visited):
        if pathIndex == len(path): return True
        #print(row, col)
        hasPath = False
        if row >= 0 and row < rows and col >= 0 and col < cols and matrix[row*cols+col] == path[pathIndex] and not visited[row][col]:
            visited[row][col] = 1
            #print('success', row, col)
            pathIndex += 1
            hasPath = self.hasPathCore(matrix, rows, cols, row, col - 1, path, pathIndex, visited) or \
                self.hasPathCore(matrix, rows, cols, row, col + 1, path, pathIndex, visited) or \
                self.hasPathCore(matrix, rows, cols, row + 1, col, path, pathIndex, visited) or \
                self.hasPathCore(matrix, rows, cols, row - 1, col, path, pathIndex, visited)
            if not hasPath:
                pathIndex -= 1  #回溯
                visited[row][col] = 0
        return hasPath
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        index = 0
        if len(matrix) == 0 or rows < 1 or cols < 1 or path == []:
            return False
        visite = [([0] * cols) for i in range(rows)]
        pathIndex = 0
        for i in range(cols):
            for j in range(rows):
                if self.hasPathCore(matrix, rows, cols, j, i, path, pathIndex, visite):
                    return True
        return False
matrix = 'ABCESFCSADEE'
rows = 3
cols = 4
path = 'ABCB'
print(Solution().hasPath(matrix, rows, cols, path))