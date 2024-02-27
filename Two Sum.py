class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numd = {}
        n = len(nums)

        for i in range(n):
            numd[nums[i]] = i # Dictionary of elements built.
        for i in range(n):
            complement = target - nums[i]
            if complement in numd and numd[complement] != i:
                return [i, numd[complement]]
        return []
  # Here we use a dictionary to store elements with their indices.
  # Then we run another loop iterating nums and check if complement (target - nums[i]) of element is present in dictionary or not and index of the complement should 
  # not be equal to the index of the first element (!=i).
  # Time complexity = O(n).
  # Space complexity = O(n)
