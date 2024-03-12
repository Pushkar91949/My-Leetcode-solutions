class Solution:
    def findSpecialInteger(self, arr):
        n = len(arr)
        step = n // 4

        for i in range(n - step):
            if arr[i] == arr[i + step]:
                return arr[i]

        return -1
# Question  link: https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/
