class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.index = 0
        self.listS = []
    def RecursionSe(self, root):
        series = ''
        if root == None:
            series += ',$'
        else:
            series += (',' + str(root.val))
            series += self.RecursionSe(root.left)
            series += self.RecursionSe(root.right)
        return series
    def Serialize(self, root):
        # write code here
        return self.RecursionSe(root)[1:]
    def RecursionDe(self):
        node = None
        if self.index < len(self.listS):
            if self.listS[self.index] == '$':
                self.index += 1
            else:
                node = TreeNode(int(self.listS[self.index]))
                self.index += 1
                node.left = self.RecursionDe()
                node.right = self.RecursionDe()
        return node
    def Deserialize(self, s):
        # write code here
        self.listS = s.split(',')
        return self.RecursionDe()
root = TreeNode(11)
root.left = TreeNode(2)
root.right = TreeNode(3)
series = Solution().Serialize(root)
print(series)
root = Solution().Deserialize(series)
print(root.val)
print(root.left.val)
print(root.right.val)
print(root.right.right)