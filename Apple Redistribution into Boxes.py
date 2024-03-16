class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        count = 0
        apples = sum(apple)
        i = 0
        if apples > 0: 
            while i < len(capacity) and apples > 0:
                apples -= capacity[i]
                count += 1
                i += 1  
        return count
# Question link: https://leetcode.com/problems/apple-redistribution-into-boxes/
