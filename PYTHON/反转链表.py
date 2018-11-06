#-*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead == None:
            return None
        if pHead.next == None:
            return pHead
        newHead = pHead
        while pHead:
            p = pHead
            pHead = pHead.next
            p.next = newHead
            newHead = p
        return newHead
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
newHead = Solution().ReverseList(head)
print(newHead.val)
print(newHead.next.val)