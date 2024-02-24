class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        numsum = sum(nums)
        tsum = (n * (n + 1)) // 2
        return tsum - numsum
