class Solution:
    def VerifyCore(self, sequence, start, end):
        #print(start, end)
        if start == end:
            return True
        root = sequence[end]
        for i in range(start, end + 1):
            if sequence[i] > root:
                break
        for j in range(i, end + 1):
            if sequence[j] < root:
                return False
        left = right = True
        if i > start:
            left = self.VerifyCore(sequence, start, i - 1)
        if i < end - 1:
            right = self.VerifyCore(sequence, i, end - 1)
        return left and right
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if sequence == []:
            return False
        return self.VerifyCore(sequence, 0, len(sequence) - 1)
sequence = [7,4,6,5]
print(Solution().VerifySquenceOfBST(sequence))
