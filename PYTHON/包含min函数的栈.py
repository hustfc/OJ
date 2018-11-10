class Solution:
    def __init__(self):
        self.stack = []
        self.minStack = []
    def push(self, node):
        # write code here
        self.stack.append(node)
        if self.minStack == []:
            self.minStack.append(node)
        else:
            min = self.minStack[len(self.minStack) - 1]
            if node <= min:
                self.minStack.append(node)
            else:
                self.minStack.append(min)
    def pop(self):
        self.stack.pop()
        self.minStack.pop()
    def top(self):
        # write code here
        return self.stack[len(self.stack) - 1]
    def min(self):
        # write code here
        return self.minStack[len(self.minStack) - 1]