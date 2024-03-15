class Solution:
    def countSegments(self, s: str) -> int:
        if not s:
            return 0
        
        count = 0
        in_segment = False
        
        for char in s:
            if char != ' ':
                if not in_segment:
                    count += 1
                    in_segment = True
            else:
                if in_segment:
                    in_segment = False
        
        return count
 #Question link: https://leetcode.com/problems/number-of-segments-in-a-string/
