class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        length = len(nums)
        u_nums = set(nums)
        missing_nums = list(set(range(1, length + 1)) - u_nums)

        return missing_nums
# Question link: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
