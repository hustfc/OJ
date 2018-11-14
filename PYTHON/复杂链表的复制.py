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
        # CloneHead = pHead.next
        # # CloneNode = CloneHead
        # while CloneNode:
        #     if CloneNode.next:
        #         CloneNode.next = CloneNode.next.next
        #     CloneNode = CloneNode.next
        # return CloneHead
        pNode = pHead
        pCloneHead = None
        pCloneNode = None
        if pNode != None:
            pCloneHead = pCloneNode = pNode.next
            pNode.next = pCloneNode.next
            pNode = pNode.next
        while pNode != None:
            pCloneNode.next = pNode.next
            pCloneNode = pCloneNode.next
            pNode.next = pCloneNode.next
            pNode = pNode.next
        return pCloneHead
    def Clone(self, pHead):
        # write code here
        if pHead == None:
            return None
        self.CloneNodes(pHead)
        self.Setrandom(pHead)
        return self.Separate(pHead)
pHead = RandomListNode(1)
print(Solution().CloneNodes(pHead).label)