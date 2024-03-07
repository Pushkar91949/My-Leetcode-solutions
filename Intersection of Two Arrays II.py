class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter_1 = Counter(nums1)
        counter_2 = Counter(nums2)
        
        intersection = counter_1 & counter_2
        
        ans = []
        for num, count in intersection.items():
            ans.extend([num] * count)
        
        return ans
