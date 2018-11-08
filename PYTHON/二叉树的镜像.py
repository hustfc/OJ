# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root == None:
            return None
        if root.left == None and root.right == None:
            return root
        root.left, root.right = self.Mirror(root.right), self.Mirror(root.left)
        return root
Root = TreeNode(8)
Root.left = TreeNode(6)
Root.right = TreeNode(10)
newRoot = Solution().Mirror(Root)
print(newRoot.left.val)
print(newRoot.right.val)
