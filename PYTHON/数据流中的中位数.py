# -*- coding:utf-8 -*-
import heapq
class Solution:
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
        self.flag = 1
    def Insert(self, num):
        # write code here
        if self.flag:
            if self.minHeap == [] or num <= self.minHeap[0]: #插入最大堆
                self.maxHeap.append(num) #插入
                heapq.heapify(self.maxHeap) #调整
            elif num > self.minHeap[0]:  #大于最小堆最小元素，需要插入到最小堆，并且替换
                self.maxHeap.append(heapq.heappop(self.minHeap))
                heapq._heapify_max(self.maxHeap)
                heapq.heappush(self.minHeap, num)
            self.flag = 0
        else:
            if self.maxHeap == [] or num >= self.maxHeap[0]:  #插入最小堆
                heapq.heappush(self.minHeap, num)
            elif num < self.maxHeap[0]: #插入最大堆，并把最大堆的根替换到右边的最小堆
                heapq.heappush(self.minHeap, heapq.heappop(self.maxHeap))  #最大堆的根
                self.maxHeap.append(num)
                heapq._heapify_max(self.maxHeap)
            self.flag = 1
    def GetMedian(self):
        # write code here
        if self.flag:
            return float('{:.2f}'.format((self.maxHeap[0] + self.minHeap[0]) / 2))
        else:
            return float('{:.2f}'.format(self.maxHeap[0]))
sol = Solution()
sol.Insert(5)
sol.Insert(2)
sol.Insert(6)
sol.Insert(7)
sol.Insert(8)
print(sol.maxHeap)
print(sol.minHeap)
print(sol.GetMedian())