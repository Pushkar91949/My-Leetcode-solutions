class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        ans = []
        d = {}
        count = 0
        for i in range(len(nums)):
            if nums[i] == x:
                count += 1
                d[count] = i
        
        for query in queries:
            if query > count:
                ans.append(-1)
            else:
                ans.append(d[query])
        
        return ans

  # Question link: https://leetcode.com/problems/find-occurrences-of-an-element-in-an-array/
