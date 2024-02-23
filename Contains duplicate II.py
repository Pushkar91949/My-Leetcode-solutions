class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d_number = {}
        for i in range(len(nums)):
            if nums[i] in d_number and i - d_number[nums[i]] <= k:
                return True
            d_number[nums[i]] = i
        return False
