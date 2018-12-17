class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        depth = 0
        if pRoot:
            depth += 1
            depth += max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right))
        return depth
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if pRoot == None:
            return True
        if abs(self.TreeDepth(pRoot.left) - self.TreeDepth(pRoot.right)) > 1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)
