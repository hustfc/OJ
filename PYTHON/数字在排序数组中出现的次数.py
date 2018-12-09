class Solution:
    def firstIndexOfK(self, data, k, start, end):
        if start > end:
            return -1
        middle = (int)((end + start) / 2)
        if data[middle] == k:
            if middle == 0 or (middle > 0 and data[middle - 1] != k):
                return middle
            else:
                end = middle - 1
        elif data[middle] < k:
            start = middle + 1
        else:
            end = middle - 1
        return self.firstIndexOfK(data, k, start, end)
    def lastIndexOfK(self, data, k, start, end):
        if start > end:
            return -1
        middle = (int)((end + start) / 2)
        if data[middle] == k:
            if middle == len(data) - 1 or(middle < len(data) - 1 and data[middle + 1] != k):
                return middle
            else:
                start = middle + 1
        elif data[middle] < k:
            start = middle + 1
        else:
            end = middle - 1
        return self.lastIndexOfK(data, k, start, end)
    def GetNumberOfK(self, data, k):
        if data == []:
            return 0
        firstIndex = self.firstIndexOfK(data, k, 0, len(data) - 1)
        lastIndex = self.lastIndexOfK(data, k, 0, len(data) - 1)
        if firstIndex == -1 or lastIndex == -1:
            return 0
        else:
            return lastIndex - firstIndex + 1
data = [1,2,3,3,3,3,4,5]
print(Solution().GetNumberOfK(data, 6))