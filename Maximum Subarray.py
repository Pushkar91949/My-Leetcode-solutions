class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -inf
        curr_sum = 0

        for i in range(len(nums)):
            curr_sum += nums[i]

            if ans < curr_sum:
                ans = curr_sum
            if curr_sum < 0:
                curr_sum = 0
        return ans

