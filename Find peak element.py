class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p=0
        if len(nums)==1:
            return 0
        elif len(nums)==2:
            return nums.index(max(nums))
        else:
            for i in range(1,len(nums)-1):
                if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                    p=i
                    break
            if p==0:
                return nums.index(max(nums))
            else:
                return p
