class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid), len(grid[0])

        def helper(r,c):
            values = set()
            for i in range(r,r+3):
                for j in range(c,c+3):
                    if grid[i][j] in values or not (1 <= grid[i][j] <= 9):
                        return 0
                    values.add(grid[i][j])
                
            for i in range(r,r+3):
                if sum(grid[i][c:c+3]) != 15:
                    return 0
            
            for i in range(c,c+3):
                if grid[r][i] + grid[r+1][i] + grid[r+2][i] != 15:
                    return 0
            
            if (
                grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != 15
                or
                grid[r+2][c] + grid[r+1][c+1] + grid[r][c+2] != 15):
                return 0
            return 1
        
        ans = 0
        for i in range(rows-2):
            for j in range(cols-2):
                ans += helper(i,j)
        return ans

# Question link: https://leetcode.com/problems/magic-squares-in-grid/
            
