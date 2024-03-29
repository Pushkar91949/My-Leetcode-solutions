class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        m = defaultdict(int)
        i, j, ans = 0, 0, 1
        while i < n and j < n:
            m[nums[j]] += 1
            while m[nums[j]] > k:
                m[nums[i]] -= 1
                i += 1
            ans = max(ans, j - i + 1)
            j += 1
        return ans
        
