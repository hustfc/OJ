class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.k = 0
    def InOrder(self, Root):
        ans = None
        if Root:
            if ans == None and Root.left:
                ans = self.InOrder(Root.left)
            if ans == None and self.k == 1:
                ans = Root
            if ans == None and self.k != 1:
                self.k -= 1
            if ans == None and Root.right:
                ans = self.InOrder(Root.right)
        return ans
    def KthNode(self, Root, k):
        if Root == None or k <= 0:
            return None
        self.k = k
        return self.InOrder(Root)
Root = TreeNode(5)
Root.left = TreeNode(3)
Root.left.left = TreeNode(2)
Root.left.right = TreeNode(4)
Root.right = TreeNode(7)
Root.right.left = TreeNode(6)
Root.right.right = TreeNode(8)
print(Solution().KthNode(Root,1).val)