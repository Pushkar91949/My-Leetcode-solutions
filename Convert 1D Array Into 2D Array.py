class Solution:
    def construct2DArray(self, o: List[int], m: int, n: int) -> List[List[int]]:
        if len(o) != m * n:
            return []
        res = []
        for i in range(m):
            res.append(o[i*n:(i+1)*n])
        return res
# Question link: https://leetcode.com/problems/convert-1d-array-into-2d-array/
