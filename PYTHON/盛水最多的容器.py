class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, j = 0, len(height) - 1
        MaxArea = (j - i) * (min(height[i], height[j]))
        while True:
            print(i, j)
            if height[i] <= height[j]:
                for m in range(i, j):
                    if height[m] > height[i]:
                        i = m
                        break
                    if m == j - 1:
                        return MaxArea
            else:
                for n in range(j, i , -1):
                    if height[n] > height[j]:
                        j = n
                        break
                    if n == i + 1:
                        return MaxArea
            Area = (j - i) * min(height[i], height[j])
            if Area > MaxArea:
                MaxArea = Area

height = [1,1]
print(Solution().maxArea(height))
