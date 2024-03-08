class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def nextMax(n, arr):
            currmax = 0
            for num in arr:
                if num != n:
                    currmax = max(currmax, num)
            return currmax
        
        while len(stones) > 1:
            if max(stones) == nextMax(max(stones), stones):
                c = nextMax(max(stones), stones)
                stones = [x for x in stones if x != max(stones) and x != c]
            else:
                a = max(stones)
                b = nextMax(a, stones)
                stones = [x for x in stones if x != a and x != b]
                stones.append(a - b)

        return stones[0] if stones else 0
# Question link: https://leetcode.com/problems/last-stone-weight/
