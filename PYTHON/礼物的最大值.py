class Solution:
    def RecursionOfValue(self, matrix, maxValueMatrix, row, col):
        maxValue = 0
        if row == 0 and col == 0:
            return matrix[0][0]
        if row >= 0 and row < len(matrix) and col >= 0 and col < len(matrix[0]):
            if row >= 1 and maxValueMatrix[row - 1][col] != 0:
                temp1 = maxValueMatrix[row - 1][col]
            else:
                temp1 = self.RecursionOfValue(matrix, maxValueMatrix, row - 1, col)
            if col >= 1 and maxValueMatrix[row][col - 1] != 0:
                temp2 = maxValueMatrix[row][col - 1]
            else:
                temp2 = self.RecursionOfValue(matrix, maxValueMatrix, row, col - 1)
            maxValue += matrix[row][col] + max(temp1, temp2)
            maxValueMatrix[row][col] = maxValue
        return maxValue
    def MaxValueOfGift(self, matrix):
        if matrix == []:
            return 0
        cols = len(matrix[0])
        rows = len(matrix)
        maxValueMatrix = [([0] * cols) for i in range(rows)]
        return self.RecursionOfValue(matrix, maxValueMatrix, rows - 1, cols - 1)
matrix = [[1,10,3,8],[12,2,9,6],[5,7,4,11],[3,7,16,5]]
print(Solution().MaxValueOfGift(matrix))
