class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        x,y = 0,1
        for i in range(2,n+1):
            curr = x + y
            x,y = y,curr
        return y
