class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        x = Counter(nums)
        xor = [y for y,count in x.items() if count == 2]
        ans = 0
        for num in xor:
            ans ^= num
        return ans
    
  # Question link: https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/description/
