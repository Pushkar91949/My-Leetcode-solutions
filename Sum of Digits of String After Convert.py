class Solution:
    def getLucky(self, s: str, k: int) -> int:
        letters = 'abcdefghijklmnopqrstuvwxyz'
        mapp = {}
        for i,char in enumerate(letters):
            mapp[char] = str(i+1)
        num = ''
        for char in s:
            num += mapp[char]
        num = int(num)
        def transform(num):
            ans = 0
            while num > 0:
                ans += num % 10
                num //= 10
            return ans
        for i in range(k):
            num = transform(num)
        return num
# Question link: https://leetcode.com/problems/sum-of-digits-of-string-after-convert/
