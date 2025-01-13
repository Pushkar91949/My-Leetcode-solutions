class Solution:
    def minimumLength(self, s: str) -> int:
        d = {}
        for char in s:
            d[char] = 1 + d.get(char, 0)
        dele = 0
        for char, count in d.items():
            if count % 2 == 0:
                dele += count - 2
            else:
                dele += count - 1
        return len(s) - dele
# Question link: https://leetcode.com/problems/minimum-length-of-string-after-operations/
