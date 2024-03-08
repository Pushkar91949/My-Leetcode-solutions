class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        l=s.split()
        pat = list(pattern)
        if len(pat) != len(l):
            return False
        map1 = {}
        ans = [0]*len(l)
        for i, word in enumerate(l):
            if word not in map1.keys() and pat[i] not in map1.values():
                map1[word] = pat[i]
        for i in range(len(l)):
            if l[i] in map1:
                ans[i] = map1[l[i]]
            else:
                ans[i] = None
        return ans == pat
            
# Question link: https://leetcode.com/problems/word-pattern/
