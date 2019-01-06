class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if pRoot == None:
            return []
        queue = []
        toPrint = 1
        queue.append(pRoot)
        nextPrint = 0
        results = []
        result = []
        while queue != []:
            popNode = queue.pop(0)
            result.append(popNode.val)
            toPrint -= 1
            if popNode.left:
                queue.append(popNode.left)
                nextPrint += 1
            if popNode.right:
                queue.append(popNode.right)
                nextPrint += 1
            if toPrint == 0:
                results.append(result)  #这层遍历完毕，加入到结果中
                toPrint = nextPrint  #下层需要遍历的数据
                result = []   #这层遍历完毕，清零
                nextPrint = 0   #下下层清零
        return results