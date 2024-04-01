class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words_dict = Counter(words)
        heap = [(-freq, word) for word, freq in words_dict.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]
 # Question link: https://leetcode.com/problems/top-k-frequent-words/
