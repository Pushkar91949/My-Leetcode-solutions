class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        
        for x in range(n + 1):
            left, right = 0, n - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] >= x:
                    right = mid - 1
                else:
                    left = mid + 1
        
            if n - left == x:
                return x
        return -1
# Question link: https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/
