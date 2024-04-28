class Solution:
    def maxPower(self, s: str) -> int:
        prev = s[0]
        count = 1
        maxcount = 1
        for i in range(1,len(s)):
            if s[i] == prev:
                count += 1
            else:
                prev = s[i]
                count = 1
            maxcount = max(count,maxcount)
        return maxcount
# Question link: https://leetcode.com/problems/consecutive-characters/
# It initializes three variables: prev to store the previous character, count to count the consecutive 
# occurrences of the current character, and maxcount to track the maximum consecutive count encountered so far, initialized to 1.
# It iterates through the characters of the input string s starting from the second character (index 1) to the end of the string.
# For each character at index i, it checks if it's the same as the previous character (prev). 
# If it is, it increments the count variable. If not, it updates prev to the current character and resets count to 1.
# During each iteration, it updates maxcount to be the maximum of the current count and the existing maxcount.
# Finally, it returns maxcount, which represents the maximum consecutive occurrences of any character within the input string.

