class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        def check(s):
            k = {1 : 'qwertyuiop',2:'asdfghjkl',3:'zxcvbnm'}
            se = set()
            for char in s:
                if char in k[1]:
                    se.add(1)
                elif char in k[2]:
                    se.add(2)
                else:
                    se.add(3)
            if len(se) == 1:
                return True
            return False
        return [x for x in words if check(x.lower())] 
# Question link: https://leetcode.com/problems/keyboard-row/
