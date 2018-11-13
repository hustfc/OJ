# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.results = []
    def Sum(self, result):
        sum = 0
        for i in result:
            sum += i
        return sum
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPathCore(self, root, expectNumber, result):
        result.append(root.val)
        Result = result[:]
        if self.Sum(result) == expectNumber and root.left == None and root.right == None:
            self.results.append(result)
        if root.left:
            self.FindPathCore(root.left, expectNumber, result)
            result = Result
        if root.right:
            self.FindPathCore(root.right, expectNumber, result)
            #result = Result
    def BubbleSort(self, results):
        for i in range(len(results)):
            for j in range(len(results) - 1, i, -1):
                if len(results[j]) > len(results[i]):
                    results[i], results[j] = results[j], results[i]
    def FindPath(self, root, expectNumber):
        # write code here
        if root == None:
            return []
        self.FindPathCore(root, expectNumber, [])
        self.BubbleSort(self.results)
        return self.results

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.right = TreeNode(3)
    root.right.right = TreeNode(2)
    root.right.right.left = TreeNode(1)
    root.right.right.right = TreeNode(5)
    expectNum = 7
    print(Solution().FindPath(root, expectNum))
