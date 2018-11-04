class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def DeleteNode(self, head, node):
        if node.next != None:
            nextNode = node.next
            node.val = nextNode.val
            node.next = nextNode.next
            del nextNode
        elif head == node:
            del node
            head = None
        else:
            p = head
            while p.next != node:
                p = p.next
            p.next = None
            del node

