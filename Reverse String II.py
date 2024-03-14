class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if k > len(s):
            return s[::-1]
        sl = list(s)
        i = 0
        while i < len(sl):
            sl[i:i+k] = sl[i:i+k][::-1]
            i += 2*k
        
        return ''.join(sl) # Question link: https://leetcode.com/problems/reverse-string-ii/
