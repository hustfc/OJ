#-*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        list = []
        result = []  #注意两个列表如果相等赋值，那么一下就会更新两个
        ####  list = result = []   !!!!错误
        if root == None:
            return list
        list.append(root)
        while list != []:
            treeNode = list.pop(0)
            result.append(treeNode.val)
            if treeNode.left:
                list.append(treeNode.left)
            if treeNode.right:
                list.append(treeNode.right)
        return result
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(Solution().PrintFromTopToBottom(root))