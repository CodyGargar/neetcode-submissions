class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxval = -1
        for x in range(len(heights) - 1):
            for y in range(x + 1, len(heights)):
                area = min(heights[x], heights[y]) * (y-x)
                if area > maxval:
                    maxval = area
        return maxval