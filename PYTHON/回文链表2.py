class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return True
        slow = fast = head #定义快慢指针来确定链表的中点
        list = []
        while fast and fast.next:
            list.insert(0, slow.val) #使用队列来模拟栈
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next  #有奇数个节点，忽略
        for val in list:
            if val != slow.val:
                return False
            slow = slow.next
        return True
