class Solution:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []
    def insert(self, x):
        if self.queue1 == []:
            self.queue2.append(x)
        elif self.queue2 == []:
            self.queue1.append(x)
    def delete(self):
        if self.queue2 == []:
            while len(self.queue1) != 1:
                self.queue2.append(self.queue1.pop(0))
            return self.queue1.pop(0)
        elif self.queue1 == []:
            while len(self.queue2) != 1:
                self.queue1.append(self.queue2.pop(0))
            return self.queue2.pop(0)
sol = Solution()
sol.insert(1)
sol.insert(2)
sol.insert(3)
print(sol.delete())
print(sol.delete())
sol.insert(5)
print(sol.delete())
print(sol.delete())
