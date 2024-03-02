class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []

        left = 0
        right = len(nums)-1
        
        while left<=right:
            if abs(nums[left])<abs(nums[right]):
                ans.append(nums[right]**2)
                right -= 1
            else:
                ans.append(nums[left]**2)
                left += 1
        return ans[::-1]
