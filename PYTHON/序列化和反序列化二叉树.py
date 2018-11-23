class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.sIndex = 0
    def recursionSerialize(self, root):
        series = ''
        if root == None:
            series += ',$'
        else:
            series += (',' + str(root.val))
            series += self.recursionSerialize(root.left)
            series += self.recursionSerialize(root.right)
        return series
    def Serialize(self, root):
        return self.recursionSerialize(root)[1:]
    def getValue(self, s, sIndex):   #处理超过10的数字，将数字字符转变为数字
        val = 0
        while ord(s[sIndex]) <= ord('9') and ord(s[sIndex]) >= ord('0'):
            val = val * 10 + int(s[sIndex])
            sIndex += 1
        return val, sIndex - 1
    def Deserialize(self, s):
        if self.sIndex < len(s):
            if s[self.sIndex] == ',':
                self.sIndex += 1
            if s[self.sIndex] == '$':
                return None
            val, self.sIndex = self.getValue(s, self.sIndex)
            treeNode = TreeNode(val)
            self.sIndex += 1
            treeNode.left = self.Deserialize(s)
            self.sIndex += 1
            treeNode.right = self.Deserialize(s)
            return treeNode
root = TreeNode(11)
root.left = TreeNode(2)
root.right = TreeNode(3)
series = Solution().Serialize(root)
print(series)
print(series.split(','))
root = Solution().Deserialize(series)
print(root.val)
print(root.left.val)
print(root.right.val)
print(root.right.right)