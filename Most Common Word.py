class Solution:
    def mostCommonWord(self, s: str, banned: List[str]) -> str:
        banned_set = set(banned)
        punctuation = "!?',;."
        for char in punctuation:
            s = s.replace(char, ' ')
        words = s.lower().split()
        word_count = {}
        for word in words:
            if word not in banned_set:
                word_count[word] = word_count.get(word, 0) + 1
        most_common_word = ""
        max_frequency = 0
        for word, frequency in word_count.items():
            if frequency > max_frequency:
                most_common_word = word
                max_frequency = frequency
        return most_common_word
