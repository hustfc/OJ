class listNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def printListFromTailToHead(self, listNode):
        lists = []
        while listNode != None:
            lists.insert(0, listNode.val)
            listNode = listNode.next
        return lists
p = ListNode(1)
p.next = ListNode(2)
p.next.next = ListNode(3)
print(Solution().printListFromTailToHead(p))