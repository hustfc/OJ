# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def Construct(self, pre, tin, startPre, endPre, startTin, endTin):
        print(startPre,endPre,startTin,endTin)
        root = TreeNode(pre[startPre])    #前序遍历第一个数字是根节点
        if startPre == endPre and startTin == endTin:   #如果只剩下一个节点了，直接返回，左子树右子树都是空
             return root
        rootIndex = startTin
        while rootIndex <= endTin and tin[rootIndex] != root.val:
            rootIndex += 1
        leftLength = rootIndex - startTin
        if leftLength > 0:   #左边大于0
            root.left = self.Construct(pre, tin, startPre + 1, startPre + leftLength, startTin, rootIndex - 1)
        if leftLength < endPre - startPre:   #pre里面存在右边子树
            root.right = self.Construct(pre, tin, startPre + leftLength + 1, endPre, rootIndex + 1, endTin)
        return root
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        return self.Construct(pre, tin, 0, len(pre) - 1, 0, len(tin) - 1)