class Solution:
    def findJudge(self, n, trust):
        count = [0] * 1001
        trustothers = set()
        
        for i in range(len(trust)):
            count[trust[i][1]] += 1
            trustothers.add(trust[i][0])
            
        for i in range(1, len(count)):
            if count[i] == n - 1 and i not in trustothers:
                return i
        
        return -1
