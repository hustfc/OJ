class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def __init__(self):
        self.lists = []
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if(listNode != None):
            if(listNode.next != None):
                self.printListFromTailToHead(listNode.next)
            self.lists.append(listNode.val)
        return self.lists
p = ListNode(1)
p.next = ListNode(2)
p.next.next = ListNode(3)
print(Solution().printListFromTailToHead(p))
