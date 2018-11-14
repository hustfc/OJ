# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def CloneNodes(self, pHead):
        pNode = pHead
        while pNode:
            CloneNode = RandomListNode(pNode.label)
            CloneNode.next = pNode.next
            CloneNode.random = None
            pNode.next = CloneNode
            pNode = CloneNode.next
        return pHead
    def Setrandom(self, pHead):
        pNode = pHead
        CloneNode = pHead.next
        while pNode:
            if pNode.random:
                CloneNode.random = pNode.random.next
            pNode = pNode.next.next
            if pNode:
                CloneNode = pNode.next
    def Separate(self, pHead):
        CloneHead = pHead.next
        CloneNode = CloneHead
        while CloneNode:
            if CloneNode.next:
                CloneNode.next = CloneNode.next.next
            CloneNode = CloneNode.next
        return CloneHead
    def Clone(self, pHead):
        # write code here
        if pHead == None:
            return None
        self.CloneNodes(pHead)
        print(pHead.label, pHead.next.label, pHead.next.next.label, pHead.next.next.next.label)
        self.Setrandom(pHead)
        return self.Separate(pHead)
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