class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        result = majority = 0

        for num in nums:
            d[num] = 1 + d.get(num, 0)
            if d[num] > majority:
                result = num
                majority = d[num]
        return result
