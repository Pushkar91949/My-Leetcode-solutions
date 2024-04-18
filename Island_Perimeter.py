class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        WATER, LAND = 0, 1
        perimeter = 0
        rows, cols = len(grid), len(grid[0])
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == LAND:
                    perimeter += 4
                    if r > 0 and grid[r - 1][c] == LAND:
                        perimeter -= 2
                    if c > 0 and grid[r][c - 1] == LAND:
                        perimeter -= 2
                        
        return perimeter
# Question link: https://leetcode.com/problems/island-perimeter/
