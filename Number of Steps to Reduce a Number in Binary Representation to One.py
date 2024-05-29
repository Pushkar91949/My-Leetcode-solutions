class Solution:
    def numSteps(self, s: str) -> int:
        def binaryToDecimal(binary):
            decimal, i = 0, 0
            while(binary != 0):
                dec = binary % 10
                decimal = decimal + dec * pow(2, i)
                binary = binary//10
                i += 1
            return decimal
    
        def iseven(n):
            if n % 2 == 0:
                return True
            return False
        s = binaryToDecimal(int(s))
        steps = 0
        while s != 1:
            if not iseven(s):
                s += 1
            else:
                s //= 2
            steps += 1
        return steps
## NAIVE SOLUTION | BEATS 99%
# Question link: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/
