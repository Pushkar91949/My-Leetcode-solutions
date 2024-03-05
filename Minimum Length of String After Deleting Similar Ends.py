class Solution:
    def minimumLength(self, s: str) -> int:
        start,end = 0,len(s) - 1
        while start < end and s[start] == s[end]:
            char = s[start]
            while start <= end and char == s[start]:
                start += 1
            while start <= end and char == s[end]:
                end -= 1
        return end - start + 1
