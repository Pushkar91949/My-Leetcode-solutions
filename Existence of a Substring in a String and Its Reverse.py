class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        t = s[::-1]
        for i in range(len(s) - 1):
            if s[i] + s[i+1] in t:
                return True
        return False # Question link: https://leetcode.com/problems/existence-of-a-substring-in-a-string-and-its-reverse/
