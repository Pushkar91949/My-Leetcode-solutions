class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count_map = {}  
        current_sum = 0  
        max_length = 0  

        for index, num in enumerate(nums):
            current_sum += 1 if num == 1 else -1  

            if current_sum == 0:
                max_length = index + 1  
            elif current_sum in count_map:
                max_length = max(max_length, index - count_map[current_sum])

            else:
                count_map[current_sum] = index

        return max_length
 # Question link: https://leetcode.com/problems/contiguous-array/
