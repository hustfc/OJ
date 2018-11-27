class Solution:
    def PartitionOfK(self, numbers, start, end, k):
        if k < 0 or numbers == [] or start < 0 or end >= len(numbers) or k > end:
            return
        low, high = start, end
        key = numbers[low]
        while low < high:
            while low < high and numbers[high] >= key:
                high -= 1
            numbers[low] = numbers[high]
            while low < high and numbers[low] <= key:
                low += 1
            numbers[high] = numbers[low]
        numbers[low] = key
        if low < k:
            self.PartitionOfK(numbers, start + 1, end, k)
        elif low > k:
            self.PartitionOfK(numbers, start, end - 1, k)
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k <= 0 or tinput == [] or k > len(tinput):
            return []
        self.PartitionOfK(tinput, 0, len(tinput) - 1, k)
        return sorted(tinput[0:k])
tinput = [1,2,3,4,5,6,7,8]
k = 8
print(Solution().GetLeastNumbers_Solution(tinput, k))