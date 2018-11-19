class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def ConvertCore(self, pRoot, lastListNode):
        if pRoot:
            if pRoot.left:
                self.ConvertCore(pRoot.left, lastListNode)
            pRoot.left = lastListNode[0]
            if lastListNode[0]:
                lastListNode[0].right = pRoot
            lastListNode[0] = pRoot
            if pRoot.right:
                self.ConvertCore(pRoot.right, lastListNode)
    def Convert(self, pRootOfTree):
        # write code here
        if pRootOfTree == None:
            return None
        lastListNode = [None]
        self.ConvertCore(pRootOfTree, lastListNode)
        while lastListNode[0].left:
            lastListNode[0] = lastListNode[0].left
        return lastListNode[0]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
left = Solution().Convert(root)
print(left.val)
print(left.right.val)
print(left.right.right.val)
