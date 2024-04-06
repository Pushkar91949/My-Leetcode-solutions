class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        openc = 0
        for i in range(len(s)):
            if s[i] == '(':
                openc += 1
            elif s[i] == ')':
                if openc == 0:
                    s[i] = '*'
                else:
                    openc -= 1
        for i in range(len(s) - 1, -1, -1):
            if openc > 0 and s[i] == "(":
                s[i] = '*'
                openc -= 1
        return ''.join(x for x in s if x != "*")
      # Question link: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
