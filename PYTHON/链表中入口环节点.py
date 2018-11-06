class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def MeetingNode(self, pHead):
        if pHead == None:
            return None
        slow = fast = pHead
        while slow and fast:
            slow = slow.next
            if slow:
                fast = fast.next.next
            if fast == slow:
                return slow
        return None
    def EntryNodeOfLoop(self, pHead):
        # write code here
        meetNode = self.MeetingNode(pHead)
        if meetNode == None:
            return None
        p, loopSize = meetNode.next, 1
        while p != meetNode:
            p = p.next
            loopSize += 1
        slow = fast = pHead
        for i in range(loopSize):
            fast = fast.next
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
head = ListNode(1)
p1 = head.next = ListNode(2)
p2 = p1.next = ListNode(3)
p3 = p2.next = ListNode(4)
p4 = p3.next = ListNode(5)
p5 = p4.next = ListNode(6)
p5.next = p5
print(Solution().EntryNodeOfLoop(head).val)