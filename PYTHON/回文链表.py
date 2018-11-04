class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def str_isPalindrome(nums, length):
    i, j = 0, length - 1
    while i != j:
        if nums[i] != nums[j]:
            return False
        if i == length / 2:
            return True
        i += 1
        j -= 1
    return True

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #脑残办法，直接将链表里面的数据放入数组中
        string = ''
        j = head
        if j == None:
            return True
        index = 0
        nums = [0] * 100000
        while j != None:
            nums[index] = j.val
            index += 1
            j = j.next
        return str_isPalindrome(nums, index)
head = ListNode(-121)
head.next = ListNode(-121)
head.next.next = ListNode(-121)
head.next.next.next = None
sol = Solution()
print(sol.isPalindrome(head))