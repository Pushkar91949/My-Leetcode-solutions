class Solution:
    def cttudents(self, students: List[int], sandwiches: List[int]) -> int:
        ct = [0, 0]
        for student in students:
            ct[student] += 1
        rem = len(sandwiches)
        for sandwich in sandwiches:
            if ct[sandwich] == 0:
                break
            if rem == 0:
                break
            ct[sandwich] -= 1
            rem -= 1
        
        return rem
