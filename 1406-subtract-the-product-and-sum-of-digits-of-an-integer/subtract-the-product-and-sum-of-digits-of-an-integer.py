class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        temp_val = n
        addition = 0
        product = 1

        while temp_val >0:
            r = temp_val % 10
            temp_val //= 10
            addition += r
            product *= r
        
        return product - addition 