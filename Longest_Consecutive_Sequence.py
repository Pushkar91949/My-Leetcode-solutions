class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        set_num = set(nums)
        for n in set_num:
            if (n-1) not in set_num:
                currlen = 1
                while (n+currlen) in set_num:
                    currlen += 1
                ans = max(ans, currlen)
        return ans # Question link: https://leetcode.com/problems/longest-consecutive-sequence/
