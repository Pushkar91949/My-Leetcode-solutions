class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxWater = 0
        while left < right:
            maxWater = max(maxWater,min(height[left],height[right]) * (right - left))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxWater
# Question link: https://leetcode.com/problems/container-with-most-water/description/
