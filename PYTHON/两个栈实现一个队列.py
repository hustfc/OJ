class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        self.stack1.append(node)
    def pop(self):
        if self.stack2 == []:
            while self.stack1 != []:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
sol = Solution()
sol.push(1)
sol.push(2)
print(sol.pop())
sol.push(3)
print(sol.pop())
print(sol.pop())
