import math
def signFunc(x):
            if x == 0:
                return 0
            elif x > 0:
                return 1
            elif x < 0:
                return -1
class Solution:
    
    def arraySign(self, nums: list[int]) -> int:
        product = math.prod(nums)
        
        return signFunc(product)