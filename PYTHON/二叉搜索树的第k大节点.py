class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.k = 0
    def recursionKthNode(self, Root):
        result = None
        if result == None and Root.left:
            result = self.recursionKthNode(Root.left)
        if result == None:
            if self.k == 1:
                return Root
            self.k -= 1
        if result == None and Root.right:
            result = self.recursionKthNode(Root.right)
        return result
    def KthNode(self, Root, k):
        if Root == None:
            return None
        self.k = k
        return self.recursionKthNode(Root)
Root = TreeNode(5)
Root.left = TreeNode(3)
Root.left.left = TreeNode(2)
Root.left.right = TreeNode(4)
Root.right = TreeNode(7)
Root.right.left = TreeNode(6)
Root.right.right = TreeNode(8)
print(Solution().KthNode(Root,3).val)
