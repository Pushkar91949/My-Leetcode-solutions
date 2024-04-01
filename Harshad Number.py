class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s = 0
        x2 = x
        while x > 0:
            s += x%10
            x //= 10
        return s if x2 % s == 0 else -1 
# Question link: https://leetcode.com/problems/harshad-number/
