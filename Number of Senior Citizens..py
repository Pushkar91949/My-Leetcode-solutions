class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for num in details:
            if int(num[-4] + num[-3]) > 60:
                count += 1
        return count
