class Solution:
    def areSentencesSimilar(self, s1: str, s2: str) -> bool:
        s1, s2 = s1.split(), s2.split()

        if len(s1) > len(s2):
            s1, s2 = s2, s1

        i = 0
        while i < len(s1) and s1[i] == s2[i]:
            i += 1
        
        j = 0
        while j < len(s1) - i and s1[-(j+1)] == s2[-(j+1)]:
            j += 1
        
        return i + j == len(s1)
# Question link: https://leetcode.com/problems/sentence-similarity-iii/description/
