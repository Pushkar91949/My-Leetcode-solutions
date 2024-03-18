class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        x = {}
        for num in nums:
            x[num] = 1 + x.get(num,0)
        for freq in x.values():
            if freq > 2:
                return False
        return True # Question link: https://leetcode.com/problems/split-the-array/
