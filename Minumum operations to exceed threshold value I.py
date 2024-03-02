class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        def greaterthank(nums,k):
            ans = True
            for num in nums:
                if num < k:
                    ans = False
            return ans
        count = 0
        a = True
        while a:
            if greaterthank(nums,k):
                return count
                a = False
            else:
                nums.remove(min(nums))
                count += 1
