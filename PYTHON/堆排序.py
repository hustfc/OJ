import heapq

data = [1,5,3,2,8,5]
heapq._heapify_max(data)
print(data)
print(heapq._heappop_max(data))
print(data)
heapq._heapreplace_max(data, 12)
print(data)
heapq.heappush(data, 15)
print(data)
heapq._heapify_max(data)
print(data)