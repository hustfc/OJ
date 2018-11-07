#-*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 == None and pHead2 == None:
            return None
        elif pHead1 == None:
            return pHead2
        elif pHead2 == None:
            return pHead1
        mergeHead = None
        if(pHead1.val <= pHead2.val):
            mergeHead = pHead1
            mergeHead.next = self.Merge(pHead1.next, pHead2)
        else:
            mergeHead = pHead2
            mergeHead.next = self.Merge(pHead1, pHead2.next)
        return mergeHead