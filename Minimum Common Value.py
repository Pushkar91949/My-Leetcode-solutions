class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i1 = i2 = 0
        l1,l2 = len(nums1),len(nums2)

        while i1 < l1 and i2 < l2:
            if nums1[i1] == nums2[i2]:
                return nums1[i1]
            elif nums1[i1] < nums2[i2]:
                i1 += 1
            else:
                i2 += 1
        return -1
    # Question link: https://leetcode.com/problems/minimum-common-value/
