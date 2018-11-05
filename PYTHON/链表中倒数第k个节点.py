#-*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head == None or k <= 0:
            return None
        i, p = 1, head
        while i < k:
            p = p.next
            if p == None:
                return None
            i += 1
        answer = head
        while p.next != None:
            answer = answer.next
            p = p.next
        return answer