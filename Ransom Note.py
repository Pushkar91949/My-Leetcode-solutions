class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dran = {}
        dmag = {}
        for char in magazine:
            dmag[char] = 1 + dmag.get(char, 0)
        for char in ransomNote:
            dran[char] = 1 + dran.get(char, 0)
        s = set(ransomNote)
        bo = True
        for char in s:
            if dran.get(char,0) > dmag.get(char,0):
                bo = False

        return bo

            
