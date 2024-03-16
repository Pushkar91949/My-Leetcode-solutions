class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        maxval = 0
        for s in strs:
            maxval = max(maxval, int(s) if s.isdigit() else len(s))
        return maxval
# Question link: https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/
