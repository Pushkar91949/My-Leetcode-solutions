class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        s = 0
        count = 0
        for num in nums:
            s += num
            if s == 0:
                count += 1
        return count # Question link: https://leetcode.com/problems/ant-on-the-boundary/
