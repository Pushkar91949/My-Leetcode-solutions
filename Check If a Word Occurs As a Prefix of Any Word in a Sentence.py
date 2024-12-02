class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        word_pos, i, n = 1, 0, len(sentence)
        while i < n:
            while i < n and sentence[i] == " ":
                i += 1
                word_pos += 1
            match_count = 0
            while i < n and match_count < len(searchWord) and sentence[i] == searchWord[match_count]:
                i += 1
                match_count += 1
            if match_count == len(searchWord):
                return word_pos
            while i < n and sentence[i] != " ":
                i += 1
        return -1
