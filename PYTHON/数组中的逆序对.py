class Solution:
    def RecursionCount(self, data, copy, start, end):
        print(start, end, data, copy)
        if start >= end:
            copy[start] = data[start]
            return 0
        count = 0
        length = int((end - start) / 2)
        leftCount = self.RecursionCount(data, copy, start, start + length)
        rightCount = self.RecursionCount(data, copy, start + length + 1, end)
        #data = copy[:]  #排序好之后，data要拷贝copy，才能保证data两边是排好序的。
        i, j = start + length, end
        copyIndex = end
        while i >= start and j >= start + length + 1:
            if data[i] > data[j]:
                copy[copyIndex] = data[i]
                copyIndex -= 1
                i -= 1
                count += (j - start - length)
            else:
                copy[copyIndex] = data[j]
                copyIndex -= 1
                j -= 1
        #比较之后，可能有一边没遍历完，copy可能没被全部填满，需要继续填充copy
        while i >= start:
            copy[copyIndex] = data[i]
            copyIndex -= 1
            i -= 1
        while j >= start + length + 1:
            copy[copyIndex] = data[j]
            copyIndex -= 1
            j -= 1
        data[start:end+1] = copy[start:end+1]
        print(start, end, data, copy)
        return leftCount + rightCount + count
    def InversePairs(self, data):
        # write code here
        if data == []:
            return 0
        #copy = data[:]
        copy = [0] * len(data)
        return (self.RecursionCount(data, copy, 0, len(data) - 1) % 1000000007)
data = [7,5,6,4]
print(Solution().InversePairs(data))