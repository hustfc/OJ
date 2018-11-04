class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        cols = len(array[0])
        rows = len(array)
        print(rows, cols)
        row, col = 0, cols - 1
        while row != rows and col != -1:
            print(row, col)
            if array[row][col] == target:
                return True
            elif array[row][col] > target:
                col -= 1
            else:
                row += 1
        return False
target = 7
array = [[1,2,8,9],[4,7,10,13]]
print(Solution().Find(target, array))