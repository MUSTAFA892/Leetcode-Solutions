class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowers_planted = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                left_empty = (i==0 or flowerbed[i-1] == 0)
                right_empty = (i == len(flowerbed)-1 or flowerbed[i+1] == 0)

                if left_empty and right_empty:
                    flowerbed[i] = 1
                    flowers_planted += 1
                
                    if flowers_planted >= n:
                        return True
                    
        return flowers_planted >= n
