class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        expcount = len(nums) // 3
        d = {}
        ans = []
        for num in nums:
            d[num] = 1 + d.get(num,0)
        for num in d:
            if d[num] > expcount:
                ans.append(num)
        return ans



        
