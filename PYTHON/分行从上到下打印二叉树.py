class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        list = []  #队列
        result = []  #每一层的结果
        results = []  #存储result的list
        nextLevel = 0
        toBeList = 1   #这层还需要加入result的元素个数
        if root == None:
            return list
        list.append(root)
        while list != []:
            treeNode = list.pop(0)
            toBeList -= 1
            result.append(treeNode.val)
            if treeNode.left:
                nextLevel += 1
                list.append(treeNode.left)
            if treeNode.right:
                nextLevel += 1
                list.append(treeNode.right)
            if toBeList == 0:
                results.append(result)
                result = []
                toBeList = nextLevel
                nextLevel = 0
        return results
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
results = Solution().PrintFromTopToBottom(root)
for i in results:
    print(i)