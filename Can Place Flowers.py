class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        length = len(flowerbed)
        i = 0

        while i < length:
            if flowerbed[i] == 0:
                if (i == 0 or flowerbed[i - 1] == 0) and (i == length - 1 or flowerbed[i + 1] == 0):
                    count += 1
                    i += 2  
                else:
                    i += 1
            else:
                i += 2  

        return count >= n
