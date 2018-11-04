#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        l3 = ListNode(0)
        tmp1 = l1
        tmp2 = l2
        tmp3 = l3
        while tmp1 != None and tmp2 != None:
            if tmp1.val + tmp2.val + carry >= 10:
                tmp3.val = tmp1.val + tmp2.val + carry - 10
                carry = 1
            else:
                tmp3.val = tmp1.val + tmp2.val + carry
                carry = 0
            tmp1 = tmp1.next
            tmp2 = tmp2.next
            if tmp1 != None and tmp2 != None:
                tmp3.next = ListNode(0)
                tmp3 = tmp3.next
        if tmp1 == None and tmp2 != None:
            while tmp2!= None:
                if tmp2.val + carry >= 10:
                    carry = 1
                    tmp3.next = ListNode(tmp2.val + carry - 10)
                else:
                    tmp3.next = ListNode(tmp2.val + carry)
                    carry = 0
                tmp3 = tmp3.next
                tmp2 = tmp2.next
        if tmp2 == None and tmp1 != None:
            while tmp1!= None:
                if tmp1.val + carry >= 10:
                    carry = 1
                    tmp3.next = ListNode(tmp1.val + carry - 10)
                else:
                    tmp3.next = ListNode(tmp1.val + carry)
                    carry = 0
                tmp3 = tmp3.next
                tmp1 = tmp1.next
        if carry == 1:
            tmp3.next = ListNode(1)
        return l3


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
sol = Solution()
l3 = sol.addTwoNumbers(l1, l2)
print(l3.val)
print(l3.next.val)
print(l3.next.next.val)






