class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        sl = len(s)
        tl = len(t)

        ps,pt = 0,0
        while ps < sl and pt < tl:
            if s[ps] == t[pt]:
                pt += 1
            ps += 1
            
        return tl - pt
    # Question link: https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/
