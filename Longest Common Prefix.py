class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        v = sorted(v)
        s = ''
        initial = v[0]
        last = v[-1]
        for i in range(min(len(initial),len(last))):
            if initial[i] != last[i]:
                return s
            s += initial[i]
        return s
# Question link: https://leetcode.com/problems/longest-common-prefix/
