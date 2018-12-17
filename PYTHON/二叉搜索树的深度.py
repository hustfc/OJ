class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        depth = 0
        if pRoot:
            depth += 1
            depth += max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right))
        return depth
