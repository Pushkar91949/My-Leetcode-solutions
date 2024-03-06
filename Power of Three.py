class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        ans = 1
        while ans < n:
            ans *= 3
        return ans == n
