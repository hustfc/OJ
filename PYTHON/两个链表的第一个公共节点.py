class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        stack1, stack2 = [], []
        if pHead1 == None or pHead2 == None:
            return None
        while pHead1:
            stack1.append(pHead1)
            pHead1 = pHead1.next
        while pHead2:
            stack2.append(pHead2)
            pHead2 = pHead2.next
        print(stack1, stack2)
        while True:
            pop1 = stack1.pop()
            pop2 = stack2.pop()
            print(pop1, pop2)
            if pop1 != pop2:
                return None
            if stack1 == [] or stack2 == [] or stack1[len(stack1) - 1] != stack2[len(stack2) - 1]:
                return pop1
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