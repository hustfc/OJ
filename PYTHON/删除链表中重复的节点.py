# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if pHead == None:
            return pHead
        preNode = None
        pNode = pHead
        while pNode:
            pNext = pNode.next
            if pNext and pNext.val == pNode.val:
                val = pNode.val
                while pNext and pNext.val == val:
                    delNode = pNext
                    pNext = pNext.next
                    del delNode
                if preNode == None:     #开头一直都错
                    pHead = pNext
                    pNode = pHead
                else:
                    preNode.next = pNext
                    pNode = pNext
            else:
                preNode = pNode
                pNode = pNode.next
        return pHead
head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(2)
newhead = Solution().deleteDuplication(head)
print(newhead.val)

