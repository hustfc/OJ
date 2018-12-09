class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        if pHead1 == None or pHead2 == None:
            return None
        length1, length2 = 0, 0
        pNode1, pNode2 = pHead1, pHead2
        while pNode1:
            length1 += 1
            pNode1 = pNode1.next
        while pNode2:
            length2 += 1
            pNode2 = pNode2.next
        if length2 >= length1:
            differLength = length2 - length1
            while differLength:
                pHead2 = pHead2.next
                differLength -= 1
        else:
            differLength = length1 - length2
            while differLength:
                pHead1 = pHead1.next
                differLength -= 1
        while pHead1 != pHead2:
            pHead1 = pHead1.next
            pHead2 = pHead2.next
        return pHead1

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node4
node2.next = node3
node3.next = node4
node4.next = node5
print(Solution().FindFirstCommonNode(node1, node2).val)
