class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        def countsort(arr):
            count = [0]*101
            for char in arr:
                count[char] += 1
            ans = []
            for i in range(101):
                ans += [i] * count[i]
            return ans

        seats = countsort(seats)
        students = countsort(students)

        ans = 0
        for i in range(len(seats)):
            ans += abs(seats[i] - students[i])
        return ans

# Question link: https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/description/
