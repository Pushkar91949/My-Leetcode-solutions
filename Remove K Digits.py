class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for i in range(len(num)):
            while stack and k > 0 and stack[-1] > num[i]:
                stack.pop()
                k -= 1
            stack.append(num[i])
        
        stack = stack[:-k] if k > 0 else stack

        res = ''.join(stack).lstrip('0')

        return res if res else '0' # Question link: https://leetcode.com/problems/remove-k-digits/
