class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        
        for op in operations:
            if op.lstrip('-').isdigit():
                record.append(int(op))
            elif op == '+':
                if len(record) >= 2:
                    record.append(record[-1] + record[-2])
            elif op == 'C':
                if record:
                    record.pop()
            elif op == 'D':
                if record:
                    record.append(2 * record[-1])
    
        return sum(record)  # Question link: https://leetcode.com/problems/baseball-game/
