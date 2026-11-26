from math import *
class Solution:
    def canAliceWin(self, n: int) -> bool:
        # if n== 10:
        #     return True
        # if n<10:
        #     return False
        stone = 10
        alice = False   

        while n>=stone:
            n -= stone
            stone -= 1
            alice = not alice
        
        return alice


        