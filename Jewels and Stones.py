class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        countstones = Counter(stones)
        count = 0
        for char in jewels:
            count += countstones.get(char, 0)
        return count
# Question link: https://leetcode.com/problems/jewels-and-stones/
