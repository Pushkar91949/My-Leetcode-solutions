class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [1]
        i2 = 0
        i3 = 0
        i5 = 0

        while len(nums) < n:
            n_2 = nums[i2] * 2
            n_3 = nums[i3] * 3
            n_5 = nums[i5] * 5
            m= min(n_2, n_3, n_5)
            if m== n_2:
                i2 += 1
            if m== n_3:
                i3 += 1
            if m== n_5:
                i5 += 1
            nums.append(m)
        return nums[-1]
