class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = []
        for i,a in enumerate(words):
            if x in a:
                ans.append(i)
        return ans # Question link: https://leetcode.com/problems/find-words-containing-character/
