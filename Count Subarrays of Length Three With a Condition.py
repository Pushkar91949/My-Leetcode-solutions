class Solution:
    def countSubarrays(self, s: List[int]) -> int:
        i, ans, j,k = 0, 0, 1, 2
        while k < len(s):
            if 2 * (s[i] + s[k]) == s[j]:
                ans += 1
            i += 1
            j += 1
            k += 1
        return ans
