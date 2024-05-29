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
#############################################################################################
# ANOTHER SOLUTION:
class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        s = list(s)
        
        while len(s) > 1:
            if s[-1] == '0':  
                s.pop() 
            else:  
                i = len(s) - 1
                while i >= 0 and s[i] == '1':
                    s[i] = '0'
                    i -= 1
                if i >= 0:
                    s[i] = '1'
                else:
                    s.insert(0, '1')
            steps += 1
        
        return steps

# Question link: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/
