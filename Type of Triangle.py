class Solution:
    def triangleType(self, nums: List[int]) -> str:
        x = len(set(nums))
        if nums[0]+nums[1] > nums[2] and nums[2]+nums[1] > nums[0] and nums[0]+nums[2] > nums[1]:
            if x == 3:
                return 'scalene'
            elif x == 2:
                return 'isosceles'
            return 'equilateral'
        return 'none'
# Question link: https://leetcode.com/problems/type-of-triangle/
