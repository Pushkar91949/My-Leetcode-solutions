class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x,y,d = 0,0,0
        direct = [[0,1],[1,0],[0,-1],[-1,0]]
        ans = 0
        obstacles = {tuple(b) for b in obstacles}
        for c in commands:
            if c == -1:
                d = (d + 1) % 4
            elif c == -2:
                d = (d - 1) % 4
            else:
                dx,dy = direct[d]
                for _ in range(c):
                    if (x+dx,y+dy) in obstacles:
                        break
                    x,y = x+dx, y+dy
            ans = max(ans, x**2 + y**2)
        return ans
# Question link: https://leetcode.com/problems/walking-robot-simulation/
