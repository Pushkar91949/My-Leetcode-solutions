class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        pointer1 = len(num1) - 1
        pointer2 = len(num2) - 1
        carry = 0
        result = []
        
        while pointer1 >= 0 or pointer2 >= 0 or carry:
            digit1 = int(num1[pointer1]) if pointer1 >= 0 else 0
            digit2 = int(num2[pointer2]) if pointer2 >= 0 else 0
            sum_digits = digit1 + digit2 + carry
            carry = sum_digits // 10
            result.append(str(sum_digits % 10))
            
            pointer1 -= 1
            pointer2 -= 1
        
        return ''.join(result[::-1])
 # Question link: https://leetcode.com/problems/add-strings/
