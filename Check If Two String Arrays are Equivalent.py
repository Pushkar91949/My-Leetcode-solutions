class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s1 = ''
        for char in word1:
            s1 += char
        s2 = ''
        for char in word2:
            s2 += char
        return s1 == s2 # Question link: https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
