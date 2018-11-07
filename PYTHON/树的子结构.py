#-*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Tree1HasTree2(self, pRoot1, pRoot2):
        if pRoot2 == None:
            return True
        elif pRoot1 == None:
            return False
        if pRoot1.val == pRoot2.val:
            return self.Tree1HasTree2(pRoot1.left, pRoot2.left) and self.Tree1HasTree2(pRoot1.right, pRoot2.right)
        else:
            return False
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if pRoot1 == None or pRoot2 == None:
            return False
        result = False
        if pRoot2.val == pRoot1.val:
            result = self.Tree1HasTree2(pRoot1, pRoot2)
        if not result:
            result = self.HasSubtree(pRoot1.left, pRoot2)
        if not result:
            result = self.HasSubtree(pRoot1.right, pRoot2)
        return result