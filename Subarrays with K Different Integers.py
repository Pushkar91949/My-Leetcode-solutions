class Solution:
    def count_subarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = 0
        r = 0
        c = 0
        f = {}
        
        while r < n:
            f[nums[r]] = f.get(nums[r], 0) + 1
            
            while len(f) > k:
                f[nums[l]] -= 1
                if f[nums[l]] == 0:
                    del f[nums[l]]
                l += 1
            
            c += r - l + 1
            r += 1
        
        return c
    
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.count_subarrays(nums, k) - self.count_subarrays(nums, k - 1) # Question link: https://leetcode.com/problems/subarrays-with-k-different-integers/
