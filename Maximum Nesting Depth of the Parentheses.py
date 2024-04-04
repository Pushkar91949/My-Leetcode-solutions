class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        maxcount = 0
        for char in s:
            if char == '(':
                count += 1
                maxcount = max(maxcount,count)
            elif char == ')':
                count -= 1
        return maxcount # Question link: https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
