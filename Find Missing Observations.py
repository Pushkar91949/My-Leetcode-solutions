class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        msum = sum(rolls)
        m = len(rolls)
        nsum = (mean * (n + m)) - msum
        if nsum > n * 6 or nsum < n:
            return []
        nmean = nsum // n
        nmod = nsum % n
        ans = [nmean] * n
        for i in range(nmod):
            ans[i] += 1
            
        return ans
# Question link: https://leetcode.com/problems/find-missing-observations/
