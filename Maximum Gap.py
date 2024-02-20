class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=[]
        nums.sort()
        if len(nums)<2:
            return 0
        else:
            for i in range(0,len(nums)-1):
                if nums[i]>nums[i+1]:
                    s.append(nums[i]-nums[i+i])
                else:
                    s.append(nums[i+1]-nums[i])
            return max(s)
