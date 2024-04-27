class Solution:
    def scoreOfString(self, s: str) -> int:
        ans = 0
        for i in range(len(s)-1):
            ans += abs(ord(s[i]) - ord(s[i+1]))
        return ans 


# Question Link: https://leetcode.com/problems/score-of-a-string/

# This code calculates the score of a string s 
# by iterating through its characters and computing the absolute difference between the ASCII values of adjacent characters.
# This difference is accumulated into a variable ans, which is then returned as the final score.
