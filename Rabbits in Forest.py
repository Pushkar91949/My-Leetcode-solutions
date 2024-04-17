class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        
        frequency = Counter(answers)
        total_rabbits = 0
        
        for answer, count in frequency.items():
            group_size = answer + 1
            groups_needed = (count + group_size - 1) // group_size
            total_rabbits += groups_needed * group_size
        
        return total_rabbits
# Question link: https://leetcode.com/problems/rabbits-in-forest/
