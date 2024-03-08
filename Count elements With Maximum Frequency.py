#from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter_nums = Counter(nums)
        maxf = max(counter_nums.values())
        ans = 0
        for val in counter_nums.values():
            if val == maxf:
                ans += val
        return ans

  # Question link: https://leetcode.com/problems/count-elements-with-maximum-frequency/
