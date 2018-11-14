class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        pNode=pHead
        while pNode!=None:
            pClone=RandomListNode(pNode.label)
            pClone.next=pNode.next
            pNode.next=pClone
            pNode=pClone.next
        self.ConnectSiblingNodes(pHead)
        return self.ReconnectNodes(pHead)
    def ConnectSiblingNodes(self,pHead):
        pNode=pHead
        while pNode!=None:
            pClone=pNode.next
            if pNode.random!=None:
                pClone.random=pNode.random.next
            pNode=pClone.next
    def ReconnectNodes(self,pHead):
        pNode=pHead
        pCloneHead=None
        pCloneNode=None
        if pNode!=None:
            pCloneHead=pCloneNode=pNode.next
            pNode.next=pCloneNode.next
            pNode=pNode.next
        while pNode!=None:
            pCloneNode.next=pNode.next
            pCloneNode=pCloneNode.next
            pNode.next=pCloneNode.next
            pNode=pNode.next
        return pCloneHead
pHead = RandomListNode(1)
pHead.next = RandomListNode(2)
pHead.next.next = RandomListNode(3)
pHead.random = pHead.next.next
pHead.next.random = pHead
newHead = Solution().Clone(pHead)
print(newHead.label, newHead.next.label, newHead.next.next.label)
print(newHead.random.label)
print(newHead.next.random.label)
print(newHead.next.next.random)
print(pHead, pHead.next, pHead.next.next)
print(newHead, newHead.next, newHead.next.next)
