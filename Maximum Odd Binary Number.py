class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count_1 = s.count('1')
        count_0 = s.count('0')

        if count_0 == 0:
            return s
        elif count_1 == 1:
            return '0' * count_0 + '1'
        else:
            return '1' * (count_1 - 1) + '0' * count_0 + '1'
