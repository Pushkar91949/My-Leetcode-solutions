class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        ans = set()
        for x,y in nums:
            for i in range(x,y+1):
                ans.add(i)
        return len(ans)
