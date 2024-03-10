class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        typesofcandies = len(set(candyType))
        if typesofcandies > len(candyType) / 2:
            return len(candyType) // 2
        return typesofcandies
# Question link: https://leetcode.com/problems/distribute-candies/
