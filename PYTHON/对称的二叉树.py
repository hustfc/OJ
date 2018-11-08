# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def sysmmetrical(self, root1, root2):
        if root1 == None and root2 == None:
            return True
        if root1 == None or root2 == None:
            return False
        if root1.val == root2.val:
            return self.sysmmetrical(root1.left, root2.right) and self.sysmmetrical(root1.right, root2.left)
        else:
            return False
    def isSymmetrical(self, pRoot):
        # write code here
        return self.sysmmetrical(pRoot, pRoot)