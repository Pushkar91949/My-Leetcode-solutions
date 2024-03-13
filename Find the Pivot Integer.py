class Solution:
    def pivotInteger(self, n: int) -> int:
        total_sum = sum(range(1, n + 1))
        left_sum = 0
        for i in range(1, n + 1):
            left_sum += i
            right_sum = total_sum - left_sum + i
            if left_sum == right_sum:
                return i
        return -1  # Question link: https://leetcode.com/problems/find-the-pivot-integer/
