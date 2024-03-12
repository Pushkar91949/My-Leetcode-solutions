class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        first_occurrence = {}
        frequency = {}
        max_degree = 0
        min_length = float('inf')

        for i, num in enumerate(nums):
            if num not in first_occurrence:
                first_occurrence[num] = i

            frequency[num] = frequency.get(num, 0) + 1
            curr_degree = frequency[num]

            if curr_degree == max_degree:
                min_length = min(min_length, i - first_occurrence[num] + 1)
            elif curr_degree > max_degree:
                max_degree = curr_degree
                min_length = i - first_occurrence[num] + 1

        return min_length if min_length != float('inf') else 0
# Question link: https://leetcode.com/problems/degree-of-an-array/
