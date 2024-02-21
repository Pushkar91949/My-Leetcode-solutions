class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        answer = []
        while columnNumber> 0:
            columnNumber-= 1
            d =columnNumber% 26
            columnNumber//= 26
            answer.append(chr(ord('A') + d))
      
        answer.reverse()
        return ''.join(answer)
