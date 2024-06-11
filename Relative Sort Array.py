class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = [0]*1001
        max1 = max(arr1)
        max2 = max(arr2)
        for char in arr1:
            count[char] += 1
        ans = []
        for char in arr2:
            ans += [char]*count[char]
            count[char] -= count[char]
        for i in range(1001):
            if count[i] != 0:
                ans += [i]*count[i]
        return ans

  # Question link: https://leetcode.com/problems/relative-sort-array/description/
