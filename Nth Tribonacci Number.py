class Solution:
    def tribonacci(self, n: int) -> int:
        if n > 3: 
            tribo = [0,1,1] + [0]*(n-2) 
            for i in range(3,len(tribo)):
                tribo[i] = tribo[i-3] + tribo[i-2] + tribo[i-1]
        else:
            tribo = [0,1,1,2]
        return tribo[n]
# Question link: https://leetcode.com/problems/n-th-tribonacci-number/
