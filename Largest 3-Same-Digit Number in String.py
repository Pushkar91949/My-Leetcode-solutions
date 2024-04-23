class Solution:
    def largestGoodInteger(self, num: str) -> str:
        count = 1
        prev_digit = num[0]
        max_good_digit = ' '
        for digit in num[1:]:
            if digit == prev_digit:
                count += 1
            else:
                count = 1
            if count == 3:
                max_good_digit = max(digit, max_good_digit)
            prev_digit = digit
        if max_good_digit == ' ':
            return ""
        return max_good_digit * 3
