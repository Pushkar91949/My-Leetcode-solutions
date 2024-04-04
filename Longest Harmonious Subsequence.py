class Solution:
    def findLHS(self, nums: List[int]) -> int:
        res = 0
        countnum = {}
        for num in nums:
            countnum[num] = countnum.get(num,0) + 1
        for num,count in countnum.items():
            if num+1 in countnum:
                res = max(countnum[num]+countnum[num+1],res)
        return res # Question link: https://leetcode.com/problems/longest-harmonious-subsequence/
