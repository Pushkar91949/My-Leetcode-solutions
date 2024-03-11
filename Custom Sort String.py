class Solution:
    def customSortString(self, order: str, s: str) -> str:
        char_count = Counter(s)
        result = []
        for char in order:
            result.append(char * char_count[char])
            char_count[char] = 0 
     
        for char, count in char_count.items():
            result.append(char * count)
        
        return ''.join(result)
  # Question link: https://leetcode.com/problems/custom-sort-string/description/
