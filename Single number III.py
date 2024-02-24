class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d = {}
        p = []
        for num in nums:
            
            d[num] = 1 + d.get(num,0)
        
        
        for num, count in d.items():
            if count == 1:
                p.append(num)
                if len(p) == 2:  
                    break
                
        return p
