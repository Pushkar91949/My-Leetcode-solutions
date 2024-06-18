class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l,r = 0, int(math.sqrt(c))
        while l <= r:
            x = l*l + r*r
            if x == c:
                return True
            elif x < c:
                l += 1
            else:
                r -= 1
        return False
