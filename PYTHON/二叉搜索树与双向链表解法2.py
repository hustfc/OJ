class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def lastElem(self, list):
        if len(list) == 0:
            return None
        else: return list[len(list) - 1]
    def ConvertCore(self, pRoot, doubleLinkedList):
        if pRoot:
            if pRoot.left:
                self.ConvertCore(pRoot.left, doubleLinkedList)
            pRoot.left = self.lastElem(doubleLinkedList)
            if self.lastElem(doubleLinkedList):
                self.lastElem(doubleLinkedList).right = pRoot
            doubleLinkedList.append(pRoot)
            if pRoot.right:
                self.ConvertCore(pRoot.right, doubleLinkedList)
    def Convert(self, pRootOfTree):
        if pRootOfTree == None:
            return None
        doubleLinkedList = []
        self.ConvertCore(pRootOfTree, doubleLinkedList)
        return doubleLinkedList[0]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(5)
root.left.right = TreeNode(4)
root.right.right = TreeNode(6)
left = Solution().Convert(root)
print(left.val)
print(left.right.val)
print(left.right.right.val)
