class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums2:
            return None
        
        next_greater_map = {}
        stack = []

        for num in nums2:
            while stack and num > stack[-1]:
                top_element = stack.pop()
                next_greater_map[top_element] = num
            
            stack.append(num)
        
        while stack:
            top_element = stack.pop()
            next_greater_map[top_element] = -1
        
        result = [next_greater_map[num] for num in nums1]
        
        return result
 # Question link: https://leetcode.com/problems/next-greater-element-i/
